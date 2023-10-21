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

