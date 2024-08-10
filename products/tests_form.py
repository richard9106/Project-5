from decimal import Decimal
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Category
from .forms import ProductManageForm

class ProductEditTest(TestCase):
    """Testing Product editing functionality"""

    def setUp(self):
        """Create a product and category instance for testing"""
        self.category = Category.objects.create(
            name='Electronics',
            friendly_name='Electronics'
        )
        self.product = Product.objects.create(
            name='Smartphone',
            sku='SP123',
            description='Latest smartphone with high-end features.',
            price=Decimal('699.99'),
            rating=Decimal('4.5'),
            image='static/images/product_images/smartphone.png',
            category=self.category
        )

    def test_product_edit_valid_form(self):
        """Test if a product is edited correctly using a valid form"""
        form_data = {
            'name': 'Smartphone Pro',
            'sku': 'SP124',
            'description': 'Updated smartphone with even more features.',
            'price': '799.99',  # Note: this is a string for form data
            'rating': '4.7',    # Note: this is a string for form data
            'category': self.category.id
        }
        
        form = ProductManageForm(data=form_data, instance=self.product)
        self.assertTrue(form.is_valid())
        form.save()

        # Refresh and check updated data
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Smartphone Pro')
        self.assertEqual(self.product.sku, 'SP124')
        self.assertEqual(self.product.description, 'Updated smartphone with even more features.')
        self.assertEqual(self.product.price, Decimal('799.99'))
        self.assertEqual(self.product.rating, Decimal('4.7'))

    def test_product_edit_invalid_form(self):
        """Test if the form is invalid with incorrect data"""
        form_data = {
            'name': '',
            'sku': 'SP125',
            'description': 'Invalid data.',
            'price': 'invalid_price',  # Invalid price
            'rating': '4.8',
            'category': self.category.id
        }
        
        form = ProductManageForm(data=form_data, instance=self.product)
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)
        self.assertIn('name', form.errors)
