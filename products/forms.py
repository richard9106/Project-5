from .models import Product, Category
from django import forms


class ProductManageForm(forms.ModelForm):
    """Edit products"""
    class Meta:
        """meta class"""
        model = Product
        fields = ['name',
                  'sku',
                  'description',
                  'price',
                  'rating',
                  'image',
                  'category'
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
  
class CategoryForm(forms.ModelForm):
    """add category form"""
    class Meta:
        model = Category
        fields = ['name', 'friendly_name']

