from django.shortcuts import render
from .models import *
from .decorators import unauthenticated_user

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


