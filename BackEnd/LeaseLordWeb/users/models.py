from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
        phone = models.CharField(max_length=50)
        email = models.CharField(max_length=100)
        vemail = models.CharField(max_length =100)
        is_tenant = models.BooleanField(default=False)
        is_landlord = models.BooleanField(default=False)

class PropertyManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='pm_profile')
    organization = models.CharField(max_length=100)

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='tenant_profile')
    propertymanager= models.ForeignKey(PropertyManager, on_delete=models.CASCADE)
    leasestart = models.DateField()
    leaseend = models.DateField()
    paymentdue = models.DateField()






# Create your models here.
