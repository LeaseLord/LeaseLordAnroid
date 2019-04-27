from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from .models import Tenant, PropertyManager
from django.contrib.auth import authenticate, login, logout
from django.template import loader, Context, Template
User = get_user_model()

def registercheck(request):
    if request.method == "POST":
        landorten = request.POST.get('landorten')
        if landorten == '1':
            return registerten(request);

        if landorten == '0':
            return registerpm(request);
    else:
        return render(request,'registration/register.html')

# This method handles the request dealing with registering a tenant
# It takes in a request, checks if it is POST and then appropriately gets data from
# the request. First check if the organization name is correct i.e
#  check whether the appropriate property manager object exists. If not then return
# a popup stating incorrect orgnization name. Otherwise,
# Fetch the appropriate property manager object, create the user using user_create
# function and then create the tenant and save it.
# If the request is not post then it renders the sign up template for tenants.
def registerten(request):
    if request.method == "POST":
        #Get data from POST
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        email = request.POST.get('email',None)
        vemail = request.POST.get('vemail',None)
        organization = request.POST.get('organization',None)

        #Check that username is not taken
        if User.objects.filter(username = username).exists():
            html = "<script> if(!alert('Username is taken!')){window.location = window.location.pathname;} </script>"
            content = loader.render_to_string('registration/register.html')
            upper,lower = content.split('</body>',1)
            upper += html
            upper += lower
            return HttpResponse(upper)

            #Check if Organization/PropertyManager exists
        if PropertyManager.objects.filter(organization=organization).exists():
            user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, password = password, email = email,is_tenant = True)
            pm = PropertyManager.objects.get(organization = organization)
            tenant = Tenant(propertymanager = pm,user = user)
            tenant.save()
            user1 = authenticate(username = username,password = password)
            login(request,user1)
            ten = Tenant.objects.get(user = request.user)
            return HttpResponseRedirect('/users/profile')
        else:
            #if it doesn't, give error
            html = "<script> if(!alert('orgnization does not exist!')){window.location = window.location.pathname;} </script>"
            content = loader.render_to_string('registration/register.html')
            upper,lower = content.split('</body>',1)
            upper += html
            upper += lower
            return render(request, 'registration/register.html')

    else:
        return render(request,'registration/register.html')

# This method handles the request that deals with registering a propertymanager
# If method is POST get all the data from POST. Check if username taken. If yes return same alert as above
# Check if organization name taken, if taken then return same error.
# If not taken create user,create property manager object and save it. Then return Thank You message
# If method is GET then just render the registerland.html page.
def registerpm(request):
    if request.method == "POST":
    #Get data from POST
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        email = request.POST.get('email',None)
        phone = request.POST.get('phone', None)
        vemail = request.POST.get('vemail',None)
        organization = request.POST.get('organization',None)


    #Check that username is not taken
        if User.objects.filter(username = username).exists():
            html = "<script> if(!alert('Username is taken!')){window.location = window.location.pathname;} </script>"
            content = loader.render_to_string('registration/register.html')
            upper,lower = content.split('</body>',1)
            upper += html
            upper += lower
            return HttpResponse(upper)

    #check that email and verify email match
        if email != vemail:
            html = "<script> if(!alert('Emails do not match')){window.location = window.location.pathname;} </script>"
            content = loader.render_to_string('registration/register.html')
            upper,lower = content.split('</body>',1)
            upper += html
            upper += lower
            return HttpResponse(upper)

        #Check if Organization/PropertyManager exists
        if PropertyManager.objects.filter(organization=organization).exists():
            html = "<script> if(!alert('Organization already exists')){window.location = window.location.pathname;} </script>"
            content = loader.render_to_string('registration/register.html')
            upper,lower = content.split('</body>',1)
            upper += html
            upper += lower
            return HttpResponse(upper)
        else:
        #if it doesn't, create user
            user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username,
                                        password = password, email = email, is_propertymanager = True, phone = phone)
            propertymanager = PropertyManager(user = user, organization = organization)
            propertymanager.save()
            user1 = authenticate(username = username,password = password)
            login(request,user1)
            pm = PropertyManager.objects.get(user=request.user)
            return HttpResponseRedirect('/users/profile')

    else:
        return render(request,'registration/register.html')


def user_login(request):

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username = username, password = password)

            if user:
                    login(request,user)
                    if user.is_tenant:
                        ten = Tenant.objects.get(user = request.user)
                        return HttpResponseRedirect('/users/profile')
                    if user.is_propertymanager:
                        pm = PropertyManager.objects.get(user=request.user)
                        return HttpResponseRedirect('/users/profile')

            else:
                return HttpResponse("Incorrect info")
        else:
            return render(request, 'registration/login.html')


def profile(request):
                    if request.user.is_tenant:
                        ten = Tenant.objects.get(user = request.user)
                        return render(request,'registration/tenantprofile.html', {'ten':ten})
                    if request.user.is_propertymanager:
                        pm = PropertyManager.objects.get(user=request.user)
                        return render(request, 'registration/pmprofile.html', {'pm':pm})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
