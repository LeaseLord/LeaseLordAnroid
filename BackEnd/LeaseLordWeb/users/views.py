from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
User = get_user_model()

def registercheck(request):
    if request.method == "POST":
        landorten = request.POST.get('landorten')
        if landorten == '1':
            return HttpResponseRedirect('/registerten')

        if landorten == '0':
                return HttpResponseRedirect('/registerland')
    else:
        return render(request,'registration/register.html')


def registerten(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        firstname = request.POST.get('first',none)
        lastname = request.POST.get('last',none)




# Create your views here.
