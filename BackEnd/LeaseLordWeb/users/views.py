from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
User = get_user_model()

def registercheck(request):
    if request.method == "POST":
        print("This runs")
        landorten = request.POST.get('landorten')
        if landorten == '1':
            return render(request,'registration/registerland.html')
            landorten = '100';
            username = request.POST.get('username',None)
            username = request.POST.get('username',None)
            username = request.POST.get('username',None)
            username = request.POST.get('username',None)
            username = request.POST.get('username',None)
            username = request.POST.get('username',None)
            username = request.POST.get('username',None)
        if landorten == '0':
            return render(request,'registration/registerten.html')





    else:
        return render(request,'registration/register.html')



# Create your views here.
