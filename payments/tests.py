from django.test import TestCase
from .models import Order
from .forms import OrderForm

class OrderFormTest(TestCase):
    """Test for the OrderForm"""

    def test_order_form_valid(self):
        """Test if the order form is valid with correct data"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890'
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_order_form_invalid(self):
        """Test if the order form is invalid with incorrect data"""
        form_data = {
            'first_name': '',  # Invalid: required field
            'last_name': 'Doe',
            'email': 'not_an_email',  # Invalid: incorrect email format
            'phone_number': ''  # Invalid: required field
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)
