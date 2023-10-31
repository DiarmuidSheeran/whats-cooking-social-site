from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *
from django.contrib.auth import views as auth_views

class TestUrls(SimpleTestCase):

    def test_landing_url_is_resolved(self):
        url = reverse('landing')
        resolved = resolve(url)
        self.assertEqual(resolved.func, landing)
        self.assertNotEqual(resolved.func, unauthenticated_user)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        resolved = resolve(url)
        self.assertEqual(resolved.func, signup)
        self.assertNotEqual(resolved.func, unauthenticated_user)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        resolved = resolve(url)
        self.assertEqual(resolved.func, user_login)
        self.assertNotEqual(resolved.func, unauthenticated_user)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        resolved = resolve(url)
        self.assertEqual(resolved.func, logoutUser)
        self.assertNotEqual(resolved.func, login_required)

    def test_follow_feed_url_is_resolved(self):
        url = reverse('follow_feed')
        resolved = resolve(url)
        self.assertEqual(resolved.func, follow_feed)
        self.assertNotEqual(resolved.func, login_required)
    
    def test_index_url_is_resolved(self):
        url = reverse('index')
        resolved = resolve(url)
        self.assertEqual(resolved.func, index)
        self.assertNotEqual(resolved.func, login_required)
    
    def test_user_profile_url_is_resolved(self):
        url = reverse('user_profile', args=['some-username'])
        resolved = resolve(url)
        self.assertEqual(resolved.func, user_profile)
        self.assertNotEqual(resolved.func, login_required)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        resolved = resolve(url)
        self.assertEqual(resolved.func, profile)
        self.assertNotEqual(resolved.func, login_required)
    
    def test_bio_is_resolved(self):
        url = reverse('bio')
        resolved = resolve(url)
        self.assertEqual(resolved.func, bio)
        self.assertNotEqual(resolved.func, login_required)

    def test_create_post_is_resolved(self):
        url = reverse('create_post')
        resolved = resolve(url)
        self.assertEqual(resolved.func, create_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_view_post_is_resolved(self):
        url = reverse('view_post', args=['some-slug'])
        resolved = resolve(url)
        self.assertEqual(resolved.func, view_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_update_posts_is_resolved(self):
        url = reverse('update_posts', args=['some-slug'])
        resolved = resolve(url)
        self.assertEqual(resolved.func, update_posts)
        self.assertNotEqual(resolved.func, login_required)

    def test_delete_post_is_resolved(self):
        url = reverse('delete_post', args=['some-slug'])
        resolved = resolve(url)
        self.assertEqual(resolved.func, delete_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_cadd_comment_to_post_is_resolved(self):
        url = reverse('add_comment_to_post', args=['some-slug'])
        resolved = resolve(url)
        self.assertEqual(resolved.func, add_comment_to_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_post_like_is_resolved(self):
        url = reverse('post_like', args=['some-slug'])
        resolved = resolve(url)
        self.assertEqual(resolved.func, post_like)
        self.assertNotEqual(resolved.func, login_required)

    def test_follow_user_is_resolved(self):
        url = reverse('follow_user', args=['some-username'])
        resolved = resolve(url)
        self.assertEqual(resolved.func, follow_user)
        self.assertNotEqual(resolved.func, login_required)

    def test_settings_is_resolved(self):
        url = reverse('settings')
        resolved = resolve(url)
        self.assertEqual(resolved.func, settings)
        self.assertNotEqual(resolved.func, login_required)

    def test_update_info_is_resolved(self):
        url = reverse('update_info')
        resolved = resolve(url)
        self.assertEqual(resolved.func, update_info)
        self.assertNotEqual(resolved.func, login_required)

    def test_delete_account_is_resolved(self):
        url = reverse('delete_account')
        resolved = resolve(url)
        self.assertEqual(resolved.func, delete_account)
        self.assertNotEqual(resolved.func, login_required)

    def test_search_users_is_resolved(self):
        url = reverse('search_results')
        resolved = resolve(url)
        self.assertEqual(resolved.func, search_users)
        self.assertNotEqual(resolved.func, login_required)

    def test_search_is_resolved(self):
        url = reverse('search')
        resolved = resolve(url)
        self.assertEqual(resolved.func, search)
        self.assertNotEqual(resolved.func, login_required)

    def test_recipe_search_is_resolved(self):
        url = reverse('recipe_search')
        resolved = resolve(url)
        self.assertEqual(resolved.func, recipe_search)
        self.assertNotEqual(resolved.func, login_required)

    def test_password_reset_sent_is_resolved(self):
        url = reverse('password_reset_done')
        resolved = resolve(url)
        self.assertEqual(resolved.func.view_class, auth_views.PasswordResetDoneView)

    def test_password_reset_is_resolved(self):
        url = reverse('reset_password')
        resolved = resolve(url)
        self.assertEqual(resolved.func.view_class, auth_views.PasswordResetView)

    def test_password_reset_form_is_resolved(self):
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        resolved = resolve(url)
        self.assertEqual(resolved.func.view_class, auth_views.PasswordResetConfirmView)

    def test_password_reset_done_is_resolved(self):
        url = reverse('password_reset_complete')
        resolved = resolve(url)
        self.assertEqual(resolved.func.view_class, auth_views.PasswordResetCompleteView)