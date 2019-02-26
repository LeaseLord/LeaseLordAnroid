# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Extends the default Django User Model to include phone number, email, verification vemail
# and the boolean tags indicating whether the user is property manager or a tenant.
class User(AbstractUser):
        phone = models.CharField(max_length=50)
        email = models.CharField(max_length=100)
        vemail = models.CharField(max_length =100)
        is_tenant = models.BooleanField(default=False)
        is_propertymanager = models.BooleanField(default=False)


# A property manager model that has a one to one relationship with the user
# and has an organization feild.
class PropertyManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='pm_profile')
    organization = models.CharField(max_length=100)
    def __str__(self):
        return self.organization


# A tenant model that has a one to one relationship with the users
# and a one to many relationship with the Property Manager meaning that
#  each property manager has multiple tenants but each tenant
# only has one property manager.
class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='tenant_profile')
    propertymanager= models.ForeignKey(PropertyManager, on_delete=models.CASCADE)
    leasestart = models.DateField(default = None,null=True)
    leaseend = models.DateField(default = None,null=True)
    paymentdue = models.DateField(default = None,null=True)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name






# Create your models here.
