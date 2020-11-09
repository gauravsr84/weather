from django.db import models

# Create your models here.
class User(models.Model):
    email_address = models.EmailField()
    password = models.CharField(max_length = 20)

class Weather(models.Model):
    area_name = models.CharField(max_length = 50, null=True)
    temperature = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    location_key = models.IntegerField(null=True)
    date_time_searched = models.DateTimeField(null=True)