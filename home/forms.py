# forms.py
from django import forms
from .models import NewsletterSubscription


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           label='Name',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control'}))


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
        }
