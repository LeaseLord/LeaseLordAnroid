from django.contrib import admin
from .models import PropertyManager
from .models import Tenant
from .models import User

admin.site.register(User)
admin.site.register(PropertyManager)
admin.site.register(Tenant)
# Register your models here.
