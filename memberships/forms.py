# memberships/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Membership


class SignupForm(forms.ModelForm):
    """Memebership form"""
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    membership_id = forms.ModelChoiceField(queryset=Membership.objects.all(), widget=forms.HiddenInput())
    card_number = forms.CharField(max_length=16)
    expiry_date = forms.CharField(max_length=5)
    address = forms.CharField(widget=forms.Textarea)


    class Meta:
        """meta class"""
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'membership_id', 'card_number', 'expiry_date', 'address']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
