from django import forms
from .models import Profile

class ProfleForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = "__all__"
