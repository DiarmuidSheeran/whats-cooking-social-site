from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ViewsTestCase(TestCase):

    def test_landing_view(self):
        # When: Accessing the landing view
        response = self.client.get(reverse('landing'))
        # Then: Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

    def test_signup_view(self):
        # Given: Form data for signing up
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'fname': 'Sammy',
            'lname': 'Sheern',
        }
        # When: Posting the signup form
        response = self.client.post(reverse('signup'), data)
        # Then: Assert that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

    def test_user_login_view(self):
        # Given: An existing user and form data for login
        User.objects.create_user(username='testuser', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        # When: Posting the login form
        response = self.client.post(reverse('login'), data)
        # Then: Assert that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

    def test_logoutUser_view(self):
        # When: Logging out the user
        response = self.client.get(reverse('logout'))
        # Then: Assert that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

    def test_index_view_logged_in(self):
        # Given: A logged-in user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(
            username='testuser',
            password='testpassword'
        )
        # When: Accessing the index view
        response = self.client.get(reverse('index'))
        # Then: Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_not_logged_in(self):
        # When: Accessing the index view without logging in
        response = self.client.get(reverse('index'))
        # Then: Assert that the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)
