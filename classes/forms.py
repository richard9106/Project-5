from django import forms
from .models import GymClass

class GymClassForm(forms.ModelForm):
    class Meta:
        model = GymClass
        fields = ['name', 'description', 'date', 'day_of_week', 'time', 'image_class']
   
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time':forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

         # Configura 'day_of_week' como solo lectura si es necesario
        if 'instance' in kwargs:
            instance = kwargs['instance']
            if instance and instance.pk:
                self.fields['day_of_week'].widget.attrs['readonly'] = True
                self.fields['day_of_week'].help_text = None