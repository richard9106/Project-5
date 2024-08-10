"""Test for form user profile info"""
from django.test import TestCase
from .forms import UserProfileForm


# Create your tests here.
class TestUserProfileForm(TestCase):
    """testing user eddit info or add info is valid"""
    def test_form_is_valid(self):
        """pased infp to the form and see if valid"""
        user_profile_form = UserProfileForm({
            'first_name': 'Juana',
            'last_name': 'Lopez',
            'phone_number': '663578594',
            'email': 'jauna@correo.com',
            'birthday': '12/06/1991'
        })
        self.assertTrue(user_profile_form.is_valid())

    def test_form_is_not_valid(self):
        """pased infp to the form and see if valid"""
        user_profile_form = UserProfileForm({
            'first_name': '',
            'last_name': '',
            'phone_number': '',
            'email': '',
            'birthday': ''
        })
        self.assertFalse(user_profile_form.is_valid())