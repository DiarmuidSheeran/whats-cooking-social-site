from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment


class CreateUserForm(UserCreationForm):
    """
    Form for creating a new user with additional fields for
    first name and last name.
    """
    fname = forms.CharField(max_length=200, required=True)
    lname = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'fname',
            'lname'
        ]


class PostForm(forms.ModelForm):
    """
    Form for creating a new post with fields for title, content,
    and featured image.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']


class BioForm(forms.ModelForm):
    """
    Form for updating user profile information, including
    bio, Twitter, Instagram and Facebook.
    """
    class Meta:
        model = UserProfile
        fields = ['bio', 'twitter', 'instagram', 'facebook']


class UpdatePostForm(ModelForm):
    """
    Form for updating an existing post with fields for
    title, content, and featured image.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']


class CommentForm(forms.ModelForm):
    """
    Form for adding a comment to a post with a field for content.
    """
    class Meta:
        model = Comment
        fields = ['content']


class UpdateForm(ModelForm):
    """
    Form for updating user information, including
    username, first name, and last name.
    """
    fname = forms.CharField(max_length=200, required=True)
    lname = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'fname', 'lname']


class UpdatePicForm(ModelForm):
    """
    Form for updating user profile picture with a field
    for profile picture.
    """
    class Meta:
        model = UserProfile
        fields = ['profile_pic']
        exclude = ['user']
