from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class LandLord(AbstractUser):
        phone = models.CharField(max_length=50)
        email = models.CharField(max_length=100)
        vemail = models.CharField(max_length =100)
        organization = models.CharField(max_length=100)

class Tenant(models.Model):
        landlord = models.ForeignKey(LandLord, on_delete=models.DO_NOTHING)
        leasestart = models.DateField()
        leaseend = models.DateField()
        paymentdue = models.DateField()


# Create your models here.
