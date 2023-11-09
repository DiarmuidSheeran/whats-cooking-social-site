from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import (
    CreateUserForm,
    PostForm,
    BioForm,
    UpdatePostForm,
    CommentForm,
    UpdateForm,
    UpdatePicForm
)
from django.http import HttpResponseRedirect
from django.urls import reverse
import os
import requests
from django.http import JsonResponse
from django.contrib import messages
from django.template.defaultfilters import filesizeformat
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
) 


# Create your views here.
@unauthenticated_user
def landing(request):
    """
    Renders the landing page.
    """
    return render(request, 'landing.html')


@unauthenticated_user
def signup(request):
    """
    Renders the sign up page.
    Allows users to input details generated by django's CreateUserForm,
    The form takes in 3 extra pieces of user data
    The Profile Picture data piece is assigned automaticaly
    The User is redirected to login page on comletion of form.
    """
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            UserProfile.objects.create(
                user=user,
                fname=fname,
                lname=lname,
                profile_pic="placeholder"
            )
            messages.success(
                request,
                'Success! ' + str(fname) +
                '. Your account has been created!'
                '<br>'
                'You can now log into your account!'
            )
            return redirect('login')
        else:
            messages.error(request, 'Account Registration error!<br>'
                                    'Please Make sure all details are valid!')

    context = {'form': form}
    return render(request, 'signup.html', context)


@unauthenticated_user
def user_login(request):
    """
    Renders the user login page.
    User is prompted to enter a valid username
    User is prompted to enter a valid password
    Request is sent to authenticate user
    If request is successful user is redirected to index page.
    If request is denied (doesnt exsit on database) login page is render
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Success ' + str(username) + '<br>'
                                      'You have logged in successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Login failed!<br>'
                                    'Username and/or Pasword is incorrect!')
            return redirect('login')

    return render(request, 'login.html')


@login_required(login_url='landing')
def logoutUser(request):
    """
    Redirects user to landing page
    """
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('landing')


@login_required(login_url='landing')
def index(request):
    """
    Renders the home page of the site.
    Searches the database for all posts.
    Orders them in order of date created on.
    Paginates the posts with 5 posts per page.
    Retrieves the requested page number from the query parameters.
    Handles exceptions for invalid page numbers or empty pages.
    Stores them in posts variable.
    posts stored in context dictionary
    context rendered with index page.
    """
    posts_list = Post.objects.all().order_by('-created_on')
    posts_per_page = 5

    paginator = Paginator(posts_list, posts_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


@login_required(login_url='landing')
def follow_feed(request):
    """
    Renders the following feed page.
    Searches the databse for all followed user of logged in user.
    Stores users in following_users Variable
    Searches the database for all posts filtered by following_user variable.
    Orders them in order of date created on.
    Stores them in posts variable.
    posts stored in context dictionary
    context rendered with follow feed page.
    """
    following_users = request.user.userprofile.following.all()
    posts_list = Post.objects.filter(user__in=following_users).order_by(
        '-created_on'
    )

    posts_per_page = 5

    paginator = Paginator(posts_list, posts_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'follow_feed.html', context)


@login_required(login_url='landing')
def profile(request):
    """
    Renders the profile page of logged in users
    Searches the database for all posts filtered by logged in user.
    Orders them in order of date created on.
    Stores them in posts variable.
    posts stored in context dictionary
    context rendered with prfoile page.

    """
    posts = Post.objects.filter(user=request.user).order_by('-created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'profile.html', context)


@login_required(login_url='landing')
def user_profile(request, username):
    """
    Renders the profile page of unauthenticated users.
    Gets the unautheticated user by username value.
    Store the user in profile_user variable.
    Searches the database for all posts filtered by profile_user variable.
    Orders them in order of date created on.
    Stores them in posts variable.
    posts and profile_user stored in context dictionary
    context rendered with user_prfoile page.
    """
    profile_user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(user=profile_user).order_by('-created_on')

    context = {
        'posts': posts,
        'profile_user': profile_user,
    }

    return render(request, 'profile_user.html', context)


@login_required(login_url='landing')
def bio(request):
    """
    Renders the bio update form page
    Takes in the authenticated user and stores them in user variable
    Gets the all objects from UserProfile model of authenticated user
    Stores them in profile variable
    Form generated from BioForm in forms.py
    Allows user to enter data to fill form
    Form contents are generated from data entered onto form fields
    Form is saved
    User is redirected back to profile page
    form and profile are stored in context dictionary
    context rendered with bio page
    """
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = BioForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.bio = form.cleaned_data.get('bio')
            profile.twitter = form.cleaned_data.get('twitter')
            profile.facebook = form.cleaned_data.get('facebook')
            profile.instagram = form.cleaned_data.get('instagram')
            profile.save()
            user.save()
            messages.success(request, 'Bio has been updated successfully')
            return redirect('profile')
    else:
        form = BioForm(instance=profile)

    context = {
               'form': form,
               'profile': profile,
               }

    return render(request, 'bio.html', context)


@login_required(login_url='landing')
def create_post(request):
    """
    Renders the create a post page.
    Takes in the authenticated user and stores them in user variable
    Form generated from PostForm in forms.py
    Checks if a file was uploaded.
    Compare the size of the uploaded file to the maximum size.
    Set the maximum file size to 10 MB in bytes.
    Once form is submitted is valid new post is created
    Post is stored and attributed to authenticated User
    User is redirected back index page.
    form is stored in context dictionary
    context rendered with create_post page
    """
    user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data.get('featured_image')
            if uploaded_file:
                max_size = 10 * 1024 * 1024
                if uploaded_file.size > max_size:
                    messages.success(request, 'File size is too large!')
                    return render(request, 'create_post.html', {'form': form})

            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'Post has been created successfully')
            return redirect('index')
        else:
            messages.error(
                request,
                'There was an error in creating you post!'
                '<br>'
                'Please ensure all text fields have content'
            )
            return redirect('create_post')

    context = {'form': form}
    return render(request, 'create_post.html', context)


@login_required(login_url='landing')
def view_post(request, slug):
    """
    Renders the post page
    The post is selected by finding the post object by it's slug
    The object is stored in the post variable
    post is stored in context dictionary
    context rendered with post page
    """
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'post.html', context)


@login_required(login_url='landing')
def update_posts(request, slug):
    """
    Renders the update_post page
    The post is selected by finding the post object by it's slug
    The object is stored in the post variable
    Form generated from UpdatePostForm in forms.py
    UpdatePostForm stored in form varibale
    Once form that is submitted is valid post is updated
    User is redirected back to view_post page via its slug.
    form and post are stored in context dictionary
    context rendered with update_post page
    """
    post = get_object_or_404(Post, slug=slug)
    form = UpdatePostForm()
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been updated successfully!')
            return redirect('view_post', slug=post.slug)
        else:
            messages.error(
                request,
                'There was an error in editing you post!'
                '<br>'
                'Please ensure all text fields have content'
            )
            return redirect('view_post', slug=post.slug)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'update_post.html', context)


@login_required(login_url='landing')
def delete_post(request, slug):
    """
    Post is selected by finding the post object by it's slug
    The object is stored in the post variable
    Checks to make sure post is users post
    If method is POST the post is deleted
    The user is redirected to index page
    If fails user is redirected to confirm_delete_post page
    """
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.user:
        if request.method == 'POST':
            post.delete()
            messages.success(request, 'Post deleted successfully!')
            return redirect('index')
        else:
            messages.error(
                request,
                'There was an error while deleting your post!'
                '<br>'
                'Please try again!'
            )
            return redirect('confirm_delete_post', slug=post.slug)


@login_required(login_url='landing')
def confirm_delete_post(request, slug):
    """
    Renders the confirm_delete_post page
    Post is selected by finding the post object by it's slug
    The object is stored in the post variable
    Post is stored in context dictionary
    Context rendered with confirm_delete_page
    """
    post = get_object_or_404(Post, slug=slug)

    context = {'post': post}
    return render(request, 'confirm_delete_post.html', context)


@login_required(login_url='landing')
def add_comment_to_post(request, slug):
    """
    Renders the add_comment_to_post update form page
    Post is selected by finding the post object by it's slug
    The object is stored in the post variable
    Form generated from CommentForm in forms.py
    Allows user to enter data to fill form
    comment variable initialised as empty
    Form contents are generated from data entered onto form field
    Form is saved
    Comment Added to post
    Comment is related to user
    User is redirected back to view_post page
    form and comment are stored in context dictionary
    context rendered with comment_to_post page
    """
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    comment = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added to post bellow!')
        return redirect('view_post', slug=post.slug)

    context = {
               'form': form,
               'comment': comment
            }
    return render(request, 'index.html', context)


@login_required(login_url='landing')
def post_like(request, slug, *args, **kwargs):
    """
    Post is selected by finding the post object by it's slug
    The object is stored in the post variable
    The likes by user on the post are initialised as False
    Checks to see if post is liked by user
    If post is liked, like is removed,
    If post is not liked, like is added
    JSON response containing the count of likes on the post returened.
    JSON response containing the current user has liked the post returened.
    """
    post = get_object_or_404(Post, slug=slug)

    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({'likes_count': post.likes.count(), 'liked': liked})


@login_required(login_url='landing')
def follow_user(request, username):
    """
    User_to_follow is selected by finding the username object
    The object is stored in the user_to_follow variable
    Followed is initialised as False
    Checks to see if user is followed by authenticated user
    If user is unfollowed, following is removed for authenticated user
    If user is unfollowed, follower is removed for diercted user
    If user is followed, following is added for authenticated user
    If user is followed, follower is added for diercted user
    JSON response containing followed returened.
    """
    user_to_follow = get_object_or_404(User, username=username)

    followed = False

    if request.user.userprofile.following.filter(
        id=user_to_follow.id
    ).exists():
        request.user.userprofile.following.remove(user_to_follow)
        user_to_follow.userprofile.followers.remove(request.user)
        followed = False
    else:
        request.user.userprofile.following.add(user_to_follow)
        user_to_follow.userprofile.followers.add(request.user)
        follwed = True

    return JsonResponse({'followed': followed})


@login_required(login_url='landing')
def settings(request):
    """
    Renders the settings page
    Authenticated user is requested
    UserPorifle is searched to find user
    Object is stored in variable profile
    UpdatePicForm is genterated from forms.py
    Form is stored in form variable
    If form is valid, redirects user to settings page
    Form and profile stored in context dictionary
    Context rendered with settings page
    """
    user = request.user
    profile = UserProfile.objects.get(user=user)
    form = UpdatePicForm()
    if request.method == 'POST':
        form = UpdatePicForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('settings')
    context = {
               'form': form,
               'profile': profile
               }
    return render(request, 'settings.html', context)


@login_required(login_url='landing')
def update_info(request):
    """
    Renders the update_info page
    Authenticated user is requested
    UserPorifle is searched to find user
    Object is stored in variable profile
    UpdateForm is genterated from forms.py
    Form is stored in form variable
    Form data got stored from data gathered by form fields
    If form is valid, redirects user to settings page
    Form and profile stored in context dictionary
    Context rendered with update_info page
    """
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.fname = form.cleaned_data.get('fname')
            profile.lname = form.cleaned_data.get('lname')
            user.username = form.cleaned_data.get('username')
            profile.save()
            user.save()
            messages.success(request, 'Account info updated successfully!')
            return redirect('settings')
    else:
        form = UpdateForm(instance=profile)

    context = {
               'form': form,
               'profile': profile,
               }
    return render(request, 'update_info.html', context)


@login_required(login_url='landing')
def delete_account(request):
    """
    Renders the delete_account page
    If request is valid deletes user
    Logs user out
    Redirects user to landing page
    """
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        messages.success(request, 'Your account has been deleted!')
        return redirect('landing')
    return render(request, 'delete_account.html')


@login_required(login_url='landing')
def search(request):
    """
    Renders the search page
    """
    return render(request, 'search.html')


@login_required(login_url='landing')
def search_users(request):
    """
    Renders the search_results page
    Extracts the value of the query parameter from the get parameters
    Results variable store all users in the database
    Check whether the query variable has a value
    results are filltered by case sentive usernames using lookup
    Results is stored in context dictionary
    Context rendered with search_results page
    """
    query = request.GET.get('query')
    results = User.objects.all()
    if query:
        results = results.filter(username__icontains=query)
    context = {'results': results}
    return render(request, 'search_results.html', context)


@login_required(login_url='landing')
def get_recipe_data(request, query):
    """
    App id is given value from env file
    App key is given value from env file
    URL defined for recipe search
    Dictionary of parameters created for the API request
    Search query and API credentials
    Request is to the Edamam API
    Check if query exists
    Check if Api response is succesfull
    """
    api_id = os.environ.get("EDAMAM_API_ID")
    api_key = os.environ.get("EDAMAM_API_KEY")

    url = "https://api.edamam.com/search"
    params = {
        "q": query,
        "app_id": api_id,
        "app_key": api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


@login_required(login_url='landing')
def recipe_search(request):
    """
    Renders the recipe_search page
    Get the q parameter from the URL's query string
    Calls the get_recipe_data function to fetch recipe data
    Recipes and Query are stored in a context dictionary
    Context rendered with recipes page
    """
    query = request.GET.get('q', '')
    if query:
        recipes = get_recipe_data(request, query)
    else:
        recipes = None

    context = {'recipes': recipes, 'query': query}
    return render(request, 'recipes.html', context)
