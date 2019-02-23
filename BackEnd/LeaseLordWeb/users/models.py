from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class LandLord(AbstractUser):
        phone = models.CharField(max_length=50)
        email = models.CharField(max_length=100)
        name = models.CharField(max_length=100)
        organization = models.CharField(max_length=100)



# Create your models here.
