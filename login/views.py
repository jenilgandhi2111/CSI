from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def index(request):
    if request.method=="POST":
        username=request.POST['stu_id']
        password=request.POST['password']
        User=authenticate(username=username,password=password)
        if User==None:
            messages.success(request,"You donot have access")
            
        else:
            login(request,User)
            messages.success(request,"You have access")
            return redirect('dashboard')
    
    return render(request,'login/index.html')


