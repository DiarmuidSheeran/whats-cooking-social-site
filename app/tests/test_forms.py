from django.test import TestCase
from django.contrib.auth.models import User
from app.forms import CreateUserForm, UpdateForm


class FormTests(TestCase):

    def test_create_user_form(self):
        # Given: Form data for creating a user
        form_data = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'fname': 'Sammy',
            'lname': 'Sheeran',
        }
        # When: Creating an instance of CreateUserForm with the given data
        form = CreateUserForm(data=form_data)
        # Then: Assert that the form is valid
        self.assertTrue(form.is_valid())

    def test_update_form(self):
        # Given: An existing user and form data for updating the user
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        form_data = {
            'username': 'testuser2',
            'fname': 'Sammy',
            'lname': 'Sheeran',
        }
        # When: Creating an instance of UpdateForm with the given data
        form = UpdateForm(data=form_data, instance=user)
        # Then: Assert that the form is valid
        self.assertTrue(form.is_valid())

