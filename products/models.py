from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    """Info of the diferent categories for our products"""

    class Meta:
        """select a name to display in admin"""
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        """returne the name"""
        return self.name

    def get_friendly_name(self):
        """get firendly name"""
        return self.friendly_name


class Product(models.Model):
    """model for products /  articles"""
    category = models.ForeignKey("Category", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0)])
    rating = models.DecimalField(max_digits=6, decimal_places=0, null=True,
                                 blank=True, validators=[MinValueValidator(0),
                                                         MaxValueValidator(5)])
    image = CloudinaryField('image', null=True, blank=True,
                             default="static/images/profile_images/default-product-image.png")

    def __str__(self):
        return self.name
