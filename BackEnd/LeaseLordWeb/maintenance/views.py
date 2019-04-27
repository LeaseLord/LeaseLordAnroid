from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from users.models import Tenant, PropertyManager
from django.template import loader
from .models import Ticket
User = get_user_model()

# Create your views here.

#This view deals with registering a new ticket in the system.
def newticket(request):
    if request.user.is_authenticated:
        if request.user.is_tenant:
            if request.method == "POST":
                username = request.user.username
                content = request.POST.get("content",None)
                subject = request.POST.get("subject",None)
                tenant1 = Tenant.objects.get(user = request.user)
                ticket = Ticket(tenant=tenant1,pm = tenant1.propertymanager,content = content,subject=subject)
                ticket.save()
                html = "<script> alert(\"Ticket Sent!\") </script>"
                content = loader.render_to_string('ticket/newticket.html')
                upper,lower = content.split('</body>',1)
                upper += html
                upper += lower
                return HttpResponse(upper)
            else:
                return render(request,'ticket/newticket.html')
        else:
            html = "<script> if(!alert('You are not signed in as a tenant')){window.location = window.location.pathname;} </script>"
            content = loader.render_to_string('ticket/newticket.html')
            upper,lower = content.split('</body>',1)
            upper += html
            upper += lower
            return HttpResponse(upper)
    else:

        return HttpResponseRedirect('/users/login')


#This function deals with sending the database data to the front end.
def displayticket(request):
    if request.user.is_authenticated:
        if request.user.is_propertymanager:
            pm1 = PropertyManager.objects.get(user=request.user)
            alltickets = Ticket.objects.all().filter(pm = pm1 )
            context = {
            'tickets' : alltickets
            }
            return render(request,'ticket/tickets.html',context)
        elif request.user.is_tenant:
            tenant1 = Tenant.objects.get(user=request.user)
            alltickets = Ticket.objects.all().filter(tenant = tenant1)
            context = {
            'tickets' : alltickets
            }
            return render(request,'ticket/tickets.html',context)
    else:
            return HttpResponseRedirect('/users/login')
