from django.db import models
from users.models import PropertyManager, Tenant, User
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class Announcement(models.Model):
    Body = models.TextField(blank = False)
    display = models.BooleanField(default = True)
    Organization = models.CharField(max_length=100)
    recievers = models.OneToOneField('users.Tenant', on_delete=models.CASCADE, null=True, related_name= 'announce')
    def __unicode__(self):
        return self.body[:50]

#    def get_abolute_url(self):
#        return reverse('announcements:single', kwargs = {'username':self.user.username, 'pk':self.pk})
