from django import forms
from classes.models import Booking, GymClass
from memberships.models import Membership
from .models import Profile


class UserProfileForm(forms.ModelForm):
    """Form to User profile page"""

    birthday = forms.DateField(
    input_formats=['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y'],  
    widget=forms.DateInput(attrs={'type': 'date'}) 
    )


    class Meta:
        """define the model and exclude user name"""
        model = Profile
        exclude = ('user', 'create_on', 'active')
        fields = ['image',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'birthday',
                  'email']

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels
            """
            super().__init__(*args, **kwargs)
            placeholder = {
                'image': 'Image Profile',
                'first_name': 'First Name',
                'last_name': 'Lirst Name',
                'email': 'Email',
                'phone_number': 'Phone Number',
                'birthday': 'Birthday',  
                }

            labels = {
                'image': 'Image Profile',
                'first_name': 'First Name',
                'last_name': 'Lirst Name',
                'email': 'Email',
                'phone_number': 'Phone Number',
                'birthday': 'Birthday',
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

            self.fields['membership'].widget.attrs.update({'class': 'form-select'})


class BookingForm(forms.ModelForm):
    """For for edit classes """
    gym_class = forms.ModelChoiceField(queryset=GymClass.objects.all(),
                                       label='Select Class')

    class Meta:
        model = Booking
        fields = ['gym_class']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gym_class'].widget.attrs.update({'class': 'form-control'})


class MembershipForm(forms.Form):
    membership = forms.ModelChoiceField(queryset=Membership.objects.all(),
                                        empty_label=None,
                                        label='Select Membership')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['membership'].widget.attrs.update({'class': 'form-select'})  
