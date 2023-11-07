from django.test import TestCase
from django.contrib.auth.models import User
from app.forms import CreateUserForm, UpdateForm

class FormTests(TestCase):

    def test_create_user_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'fname': 'Sammy',
            'lname': 'Sheeran',
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_form(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        form_data = {
            'username': 'testuser2',
            'fname': 'Sammy',
            'lname': 'Sheeran',
        }
        form = UpdateForm(data=form_data, instance=user)
        self.assertTrue(form.is_valid())
