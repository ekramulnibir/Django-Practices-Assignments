from django import forms
from first_app.models import StudentRegistrationModel

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistrationModel
        fields = '__all__'

        labels = {
            'name' : 'Student Name',
            'email' : 'Student Email',
            'address': 'Address'
        }

        help_texts = {
            'name' : "Write your full name",
            'email' : "Write your email here",
            'address' : "Write your address here"
        }

        error_messages = {
            'name' : {'required' : 'Name is required'},
            'email' : {'required' : 'Email is required'},
        }

        widgets = {
            'date_field': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_time_field': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'decimal_field': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter decimal value'}),
            'time_field': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
