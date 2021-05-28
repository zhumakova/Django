from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Service
from  .models import Master
from .services import profileCreate


def homepage(request):
    return HttpResponse(f'Welcome to our site, {request.user}')

def services(request):
    services = Service.objects.all()
    return render(request,'service.html',{'services':services})

def masters(request):
    masters = Master.objects.all()
    return render(request,'master.html',{'masters':masters})

def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            profileCreate(form.cleaned_data,form.instance)
    return render(request,'register.html',{'form':form})



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('home')
    return render(request,'login.html')

def master_detail(request,master_id):
    try:
        master = Master.objects.get(id=master_id)
        services=master.services.all()
        certificates=master.certificates_set.all()
    except Master.DoesNotExist:
        return HttpResponse(404)
    return render(request,'master_detail.html',{'master':master,
                                                'services':services,'certificates':certificates})