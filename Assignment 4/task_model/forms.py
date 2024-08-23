from django import forms
from .models import TaskModel

class TaskModelForm(forms.ModelForm):
    assign_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = TaskModel
        fields = "__all__"
