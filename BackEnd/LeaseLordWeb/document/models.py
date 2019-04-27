from django.db import models
from users.models import Tenant, PropertyManager
# Create your models here.

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant,related_name="ten",on_delete=models.CASCADE)
    pm = models.ForeignKey(PropertyManager,related_name="propm",on_delete=models.CASCADE)
    lease = models.FileField(upload_to='leases/')
