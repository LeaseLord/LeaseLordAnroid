from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
User = get_user_model()

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        name = request.POST.get('name',None)
        phone = request.POST.get('phone',None)
        email = request.POST.get('email',None)
        organization = request.POST.get('organization',None)
        User.objects.create_user(username=username, password=password, email=email,phone = phone,organization = organization)
        return HttpResponseRedirect('/')
    else:
        return render(request,'registration/register.html')


# Create your views here.
