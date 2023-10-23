from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('signup/', views.signup , name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('index/', views.index, name="index"),
    path('profile/<str:username>/', views.user_profile , name="user_profile"),
    path('profile/', views.profile , name="profile"),
    path('bio/', views.bio , name="bio"),
    path('create_post/', views.create_post , name="create_post"),
    path('post/<slug:slug>', views.view_post , name="view_post"),
]