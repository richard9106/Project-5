from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    """Form to User profile page"""

    class Meta:
        """define the model and exclude user name"""
        model = CustomUser
        exclude = ('username', 'create_on', 'completed_info')

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
                }

            labels = {
                'first_name': 'First Name',
                'last_name': 'Lirst Name',
                'email': 'Email',
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