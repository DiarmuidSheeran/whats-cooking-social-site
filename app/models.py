from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    profile_pic = CloudinaryField('image', default='placeholder')
    followers = models.ManyToManyField(User, related_name='following_users', blank=True)
    following = models.ManyToManyField(User, related_name='followers', blank=True)
    bio = models.TextField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

    def follow(self, user_to_follow):
        self.following.add(user_to_follow)

    def unfollow(self, user_to_unfollow):
        self.following.remove(user_to_unfollow)

    def follower(self, followers):
        self.followers.add(followers)
