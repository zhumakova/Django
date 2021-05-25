from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Service
from .models import Master
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

def homepage(request):
    return HttpResponse ('Welcome!:)')

def services(request):
    services=Service.objects.all()
    return render(request,'service.html',{'services':services})

def masters(request):
    masters=Master.objects.all()
    return  render(request,'Masters.html',{'masters':masters})

def register_page(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'register.html',{'form':form})

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request,'login.html')

def master_detail(request,master_id):
    try:
        master=Master.objects.get(id=master_id)
    except Master.DoesNotExist:
        return HttpResponse('404')
    return render(request,'master_detail.html',{'master':master})