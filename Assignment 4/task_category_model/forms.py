from django import forms
from .models import TaskCategoryModel

class TaskCategoryModelForm(forms.ModelForm):
    
    class Meta:
        model = TaskCategoryModel
        fields = "__all__"
