from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from users.models import Tenant, PropertyManager
from django.template import loader
from .models import Lease

# Create your views here.
def UploadLease(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.is_propertymanager:
                pm1 = PropertyManager.objects.get(user=request.user)
                id = request.POST.get('tenant',None)
                tenant = Tenant.objects.get(id = id)
                document = request.FILES['document']
                lease = Lease(tenant=tenant,pm=pm1,lease=document)
                lease.save()
                html = "<script> if(!alert('File Uplaoded!')){window.location = window.location.pathname;} </script>"
                content = loader.render_to_string('sharedoc/documents.html')
                upper,lower = content.split('</body>',1)
                upper += html
                upper += lower
                return HttpResponse(upper)
    else:
        if request.user.is_authenticated:
            pm1 = PropertyManager.objects.get(user=request.user)
            return render(request,'sharedoc/documents.html',{'pm':pm1})
        else:
            return HttpResponseRedirect('/login')

def ViewLeases(request):
    if request.user.is_authenticated:
        if request.user.is_propertymanager:
            pm1 = PropertyManager.objects.get(user=request.user)
            return render(request,'sharedoc/viewdocuments.html',{'pm':pm1})
        else:
            tenant = Tenant.objects.get(user=request.user)
            lease = Lease.objects.get(tenant=tenant)
            return render(request,'sharedoc/viewdocuments.html',{'tenant':tenant, 'lease':lease})
    else:
        return HttpResponseRedirect('/login')
