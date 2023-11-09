from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):

    def test_landing_url_is_resolved(self):
        # Given: Landing URL
        url = reverse('landing')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, landing)
        self.assertNotEqual(resolved.func, unauthenticated_user)

    def test_signup_url_is_resolved(self):
        # Given: Signup URL
        url = reverse('signup')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, signup)
        self.assertNotEqual(resolved.func, unauthenticated_user)

    def test_login_url_is_resolved(self):
        # Given: login URL
        url = reverse('login')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, user_login)
        self.assertNotEqual(resolved.func, unauthenticated_user)

    def test_logout_url_is_resolved(self):
        # Given: logout URL
        url = reverse('logout')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, logoutUser)
        self.assertNotEqual(resolved.func, login_required)

    def test_follow_feed_url_is_resolved(self):
        # Given: follow_feed URL
        url = reverse('follow_feed')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, follow_feed)
        self.assertNotEqual(resolved.func, login_required)

    def test_index_url_is_resolved(self):
        # Given: index URL
        url = reverse('index')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, index)
        self.assertNotEqual(resolved.func, login_required)

    def test_user_profile_url_is_resolved(self):
        # Given: user_profile URL
        url = reverse('user_profile', args=['some-username'])
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, user_profile)
        self.assertNotEqual(resolved.func, login_required)

    def test_profile_url_is_resolved(self):
        # Given: profile URL
        url = reverse('profile')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, profile)
        self.assertNotEqual(resolved.func, login_required)

    def test_bio_is_resolved(self):
        # Given: bio URL
        url = reverse('bio')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, bio)
        self.assertNotEqual(resolved.func, login_required)

    def test_create_post_is_resolved(self):
        # Given: create_post URL
        url = reverse('create_post')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, create_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_view_post_is_resolved(self):
        # Given: view_post URL
        url = reverse('view_post', args=['some-slug'])
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, view_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_update_posts_is_resolved(self):
        # Given: update_post URL
        url = reverse('update_posts', args=['some-slug'])
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, update_posts)
        self.assertNotEqual(resolved.func, login_required)

    def test_delete_post_is_resolved(self):
        # Given: delete_post URL
        url = reverse('delete_post', args=['some-slug'])
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, delete_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_cadd_comment_to_post_is_resolved(self):
        # Given: add_comment_to_post URL
        url = reverse('add_comment_to_post', args=['some-slug'])
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, add_comment_to_post)
        self.assertNotEqual(resolved.func, login_required)

    def test_post_like_is_resolved(self):
        # Given: post_like URL
        url = reverse('post_like', args=['some-slug'])
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, post_like)
        self.assertNotEqual(resolved.func, login_required)

    def test_follow_user_is_resolved(self):
        # Given: follow_user URL
        url = reverse('follow_user', args=['some-username'])
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, follow_user)
        self.assertNotEqual(resolved.func, login_required)

    def test_settings_is_resolved(self):
        # Given: setting URL
        url = reverse('settings')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, settings)
        self.assertNotEqual(resolved.func, login_required)

    def test_update_info_is_resolved(self):
        # Given: update_info URL
        url = reverse('update_info')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, update_info)
        self.assertNotEqual(resolved.func, login_required)

    def test_delete_account_is_resolved(self):
        # Given: delete_account URL
        url = reverse('delete_account')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, delete_account)
        self.assertNotEqual(resolved.func, login_required)

    def test_search_users_is_resolved(self):
        # Given: search_results URL
        url = reverse('search_results')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, search_users)
        self.assertNotEqual(resolved.func, login_required)

    def test_search_is_resolved(self):
        # Given: search URL
        url = reverse('search')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, search)
        self.assertNotEqual(resolved.func, login_required)

    def test_recipe_search_is_resolved(self):
        # Given: recipe_search URL
        url = reverse('recipe_search')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(resolved.func, recipe_search)
        self.assertNotEqual(resolved.func, login_required)

    def test_password_reset_sent_is_resolved(self):
        # Given: password_reset_done URL
        url = reverse('password_reset_done')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(
            resolved.func.view_class,
            auth_views.PasswordResetDoneView
        )

    def test_password_reset_is_resolved(self):
        # Given: reset_password URL
        url = reverse('reset_password')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(
            resolved.func.view_class,
            auth_views.PasswordResetView
        )

    def test_password_reset_form_is_resolved(self):
        # Given: reset_password_confirm URL
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(
            resolved.func.view_class,
            auth_views.PasswordResetConfirmView
        )

    def test_password_reset_done_is_resolved(self):
        # Given: password_reset_complete URL
        url = reverse('password_reset_complete')
        # When: Resolving the URL
        resolved = resolve(url)
        # Then: Assert that the correct view function is called
        self.assertEqual(
            resolved.func.view_class,
            auth_views.PasswordResetCompleteView
        )
