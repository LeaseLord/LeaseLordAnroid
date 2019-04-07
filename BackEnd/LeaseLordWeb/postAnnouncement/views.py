from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Announcement
from django.template import loader
from users.models import User, PropertyManager, Tenant
from django.views import generic
from django.http import Http404
from . import models
from django.contrib.auth import get_user_model

def post(request):
    if request.method == "POST":
        if request.user.is_propertymanager:
            user = request.user
            userorganization = PropertyManager.objects.filter(user = user).first()
            body = request.POST.get('message', None)
            tenants = Tenant.objects.get(propertymanager = userorganization)
            announcement1 = Announcement(Body = body, Organization = userorganization, recievers = tenants)
            announcement1.save()
            return HttpResponse("Announcement posted!")
        else:
           return HttpResponse("Unable to post, you are not a property manager")

    else:
         return render(request,'postannouncement/post.html')
