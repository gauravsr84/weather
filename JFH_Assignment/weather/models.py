from django.db import models

# Create your models here.
class User(models.Model):
    email_address = models.EmailField()
    password = models.CharField(max_length = 20)
    
