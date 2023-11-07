from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import render
from django.conf.urls import handler404

urlpatterns = [
    path('', views.landing, name="landing"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('index/', views.index, name="index"),
    path('follow_feed/', views.follow_feed, name="follow_feed"),
    path('profile/<str:username>/', views.user_profile, name="user_profile"),
    path('profile/', views.profile, name="profile"),
    path('bio/', views.bio, name="bio"),
    path('create_post/', views.create_post, name="create_post"),
    path('post/<slug:slug>', views.view_post, name="view_post"),
    path('update_post/<slug:slug>/', views.update_posts, name="update_posts"),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),
    path(
        'confirm_delete_post/<slug:slug>/',
        views.confirm_delete_post,
        name='confirm_delete_post'
    ),
    path(
        'index/<slug:slug>/',
        views.add_comment_to_post,
        name='add_comment_to_post'
    ),
    path('index/<slug:slug>/like/', views.post_like, name='post_like'),
    path(
        'index/<str:username>/follow/',
        views.follow_user,
        name='follow_user'
    ),
    path('settings/', views.settings, name="settings"),
    path('update_info/', views.update_info, name="update_info"),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('search/', views.search_users, name='search_results'),
    path('search/users', views.search, name='search'),
    path('recipes/', views.recipe_search, name='recipe_search'),

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view
        (template_name="password_reset.html"),
        name="reset_password"
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view
        (template_name="password_reset_sent.html"),
        name="password_reset_done"
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view
        (template_name="password_reset_form.html"),
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view
        (template_name="password_reset_done.html"),
        name="password_reset_complete"
    ),
]

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404