from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=32)