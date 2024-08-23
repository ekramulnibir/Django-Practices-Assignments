from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    album_relase_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    ratings = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Album
        fields = '__all__'