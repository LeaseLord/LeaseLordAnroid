from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from users.models import Tenant, PropertyManager
from django.template import loader
from .models import Announcement
User = get_user_model()

# Create your views here.

#This view deals with creating a new announcement in the system.
def postAnnouncement(request):
    if request.user.is_authenticated:
        if request.user.is_propertymanager:
            if request.method == "POST":
                username = request.user.username
                content = request.POST.get("content",None)
                subject = request.POST.get("subject",None)
                pm1 = PropertyManager.objects.get(user = request.user)
                announcement = Announcement(pm = pm1 ,content = content,subject=subject)
                announcement.save()
                html = "<script> alert(\"Announcement Sent!\") </script>"
                content = loader.render_to_string('Announce/announcement.html')
                upper,lower = content.split('</body>',1)
                upper += html
                upper += lower
                return HttpResponse(upper)
            else:
                return render(request,'ticket/newticket.html')
        else:
            html = "<script> alert(\"You are not signed in as a landlord.\") </script>"
            content = loader.render_to_string('ticket/newticket.html')
            upper,lower = content.split('</body>',1)
            upper += html
            upper += lower
            return HttpResponse(upper)
    else:

        return HttpResponseRedirect('/users/login')


#This function deals with sending the database data to the front end.
def displayannouncement(request):
    if request.user.is_authenticated:
        if request.user.is_tenant:
            ten = Tenant.objects.get(user=request.user)
            pm1 =  ten.propertymanager
            allannouncements = Announcement.objects.all().filter(pm = pm1 )
            context = {
            'announcements' : allannouncements
            }
            return render(request,'Announce/announcement.html',context)
        elif request.user.is_propertymanager:
            pm1 = PropertyManager.objects.get(user=request.user)
            allannouncements = Announcement.objects.all().filter(pm = pm1)
            context = {
            'announcements' : allannouncements
            }
            return render(request,'Announce/announcement.html',context)
    else:
            return HttpResponseRedirect('/users/login')
