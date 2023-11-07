from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ViewsTestCase(TestCase):

    def test_landing_view(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

    def test_signup_view(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'fname': 'Sammy',
            'lname': 'Sheern',
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)

    def test_user_login_view(self):
        User.objects.create_user(username='testuser', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)

    def test_logoutUser_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_index_view_logged_in(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_not_logged_in(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)