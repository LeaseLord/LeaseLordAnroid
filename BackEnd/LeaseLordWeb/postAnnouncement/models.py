from django.db import models
from users.models import Tenant, PropertyManager

# Create your models here.

#Announcement model that has a tenant and pm as foreign key.
#It has a subject and content
class Announcement(models.Model):
    pm = models.ForeignKey(PropertyManager,related_name="pm1",on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=500, default = 'invalid annuncement')
    created_at = models.DateTimeField(auto_now_add = True)
