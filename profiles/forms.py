from classes.models import Booking
from memberships.models import Membership
from django import forms
from .models import Profile


class UserProfileForm(forms.ModelForm):
    """Form to User profile page"""

    class Meta:
        """define the model and exclude user name"""
        model = Profile
        exclude = ('user', 'create_on', 'active')

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels
            """
            super().__init__(*args, **kwargs)
            placeholder = {
                'first_name': 'First Name',
                'last_name': 'Lirst Name',
                'email': 'Email',
                'my_memberships': 'My membership'       
                }

            labels = {
                'first_name': 'First Name',
                'last_name': 'Lirst Name',
                'email': 'Email',
                'my_memberships': 'My membership'  
                
            }

            

            for field in self.fields:
                if field in placeholder:
                    if self.fields[field].required:
                        placeholder = f'{placeholder[field]} *'
                    else:
                        placeholder = placeholder[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                if field in labels:
                    self.fields[field].label = labels[field]


class BookingForm(forms.ModelForm):
    """For for edit classes """
    class Meta:
        model = Booking
        fields = ['gym_class']  # Los campos que deseas permitir que se editen

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalización opcional de los widgets o validaciones adicionales
        
        
class MembershipForm(forms.Form):
    membership = forms.ModelChoiceField(queryset=Membership.objects.all(), empty_label=None, label='Select Membership')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['membership'].widget.attrs.update({'class': 'form-select'})  # Añadir clases CSS si es necesario