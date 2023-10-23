from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('signup/', views.signup , name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('index/', views.index, name="index"),
]