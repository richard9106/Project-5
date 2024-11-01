from decimal import Decimal
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Category
from .forms import ProductManageForm
from PIL import Image
import io

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

    def generate_test_image(self):
        """Generate a simple image for testing purposes"""
        image = Image.new('RGB', (100, 100), color='red')
        image_io = io.BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        return SimpleUploadedFile(
            name='test_image.jpg',
            content=image_io.read(),
            content_type='image/jpeg'
        )

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

    def test_product_edit_valid_form(self):
        """Test if a product is edited correctly using a valid form"""
        image_file = self.generate_test_image()  # Use the method to generate an image

        form_data = {
            'name': 'Smartphone Pro',
            'sku': 'SP124',
            'description': 'Updated smartphone with even more features.',
            'price': '799.99',
            'rating': '4',
            'category': self.category.id
        }

        form_files = {'image': image_file}
        form = ProductManageForm(data=form_data, files=form_files, instance=self.product)
        
        # Imprimir errores de validación para depuración
        print(form.errors)
        self.assertTrue(form.is_valid())
        form.save()

        # Refresh and check updated data
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Smartphone Pro')
        self.assertEqual(self.product.sku, 'SP124')
        self.assertEqual(self.product.description, 'Updated smartphone with even more features.')
        self.assertEqual(self.product.price, Decimal('799.99'))
        self.assertEqual(self.product.rating, Decimal('4'))
