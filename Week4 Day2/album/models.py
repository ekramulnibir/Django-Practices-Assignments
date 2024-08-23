from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_relase_date = models.DateField()
    ratings = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.album_name} - {self.musician.first_name}'
