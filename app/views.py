from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import CreateUserForm, PostForm

# Create your views here.
@unauthenticated_user
def landing(request):
    return render(request, 'landing.html')

@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            UserProfile.objects.create(user=user, fname=fname, lname=lname, profile_pic="placeholder")
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'login.html')

@login_required(login_url='landing')
def logoutUser(request):
    logout(request)
    return redirect('landing')

@login_required(login_url='landing')
def index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

@login_required(login_url='landing')
def profile(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'profile.html', context)

def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(user=profile_user).order_by('-created_on')

    context = {
        'posts': posts,
        'profile_user': profile_user,
    }

    return render(request, 'profile_user.html', context)

def bio(request):
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
    user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'create_post.html', context)

   




