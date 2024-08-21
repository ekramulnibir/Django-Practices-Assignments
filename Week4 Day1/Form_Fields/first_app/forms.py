from django import forms
from django.core import validators
import datetime


class RegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    agree = forms.BooleanField()
    # date = forms.DateField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    value = forms.DecimalField()

    comment = forms.CharField(max_length=10)
    email = forms.EmailField(
        label="Please enter your email address",
    )

    first_name = forms.CharField(initial="Your name")
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)

    FAVORITE_COLORS_CHOICES = [
        ("b", "Blue"),
        ("g", "Green"),
        ("w", "White"),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    fav_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    Multiple_favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    Radio_Multiple_favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

