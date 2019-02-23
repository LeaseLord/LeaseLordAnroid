from django.contrib import admin
from .models import LandLord
from .models import Tenant

admin.site.register(LandLord)
admin.site.register(Tenant)
# Register your models here.
