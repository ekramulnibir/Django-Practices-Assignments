from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    instrument_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

