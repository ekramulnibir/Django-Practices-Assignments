from django.db import models

# Create your models here.
class StudentRegistrationModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.TextField()

    big_integer_field = models.BigIntegerField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    # duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    positive_big_integer_field = models.PositiveBigIntegerField()
    time_field = models.TimeField()



    