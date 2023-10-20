from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class CreateUserForm(UserCreationForm):
    fname = forms.CharField(max_length=200, required=True)
    lname = forms.CharField(max_length=200, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'fname', 'lname']