from django.db import models
from users.models import Tenant, PropertyManager

# Create your models here.

#Ticket Model that has a tenant and pm as foreign key.
#It has a subject, content and a boolean determining if the ticket is resolved or not.
class Ticket(models.Model):
    tenant = models.ForeignKey(Tenant,related_name="tenant",on_delete=models.CASCADE)
    pm = models.ForeignKey(PropertyManager,related_name="pm",on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    is_resolved = models.BooleanField(default=False)
