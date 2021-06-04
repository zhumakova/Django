from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile,Order
from spa.models import Service
from .forms import OrderForm,ProfileForm
from .services import * #incrementOrderCount,countMoney,time_check
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser

def profile_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
        count_sale(profile)
    except (Profile.DoesNotExist,TypeError):
        return HttpResponse('404')
    form=ProfileForm(instance=profile)
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    return render(request,'profile.html',{'profile':profile,'form':form})

def order_page(request,service_id):
    service=Service.objects.get(id=service_id)
    user = request.user
    form = OrderForm(initial={'user':user,'service':service})
    if request.method == "POST":
        form = OrderForm(request.POST,initial={'user':user})
        if form.is_valid():
            incrementOrderCount(user.profile)
            countMoney(user.profile,form.instance)
            form.save()
    return render(request,'order.html',{'form':form,'service': service})

def my_orders(request):
    user=request.user
    if isinstance(user,AnonymousUser):
        return HttpResponse('Login please!')
    orders = Order.objects.filter(user=user)
    return render(request,'my_orders.html',{'orders':orders})


def delete_order(request,order_id):
    try:
        order = Order.objects.get(user=request.user,id=order_id)
    except Order.DoesNotExist:

        return HttpResponse('?')
    if request.method == 'POST':

        order_date=order.date_created

        if  time_check(order_date):
            order.delete()
        else:
            return HttpResponse('Time is UP!')

    return render(request,'delete_order.html')

def update_order(request,order_id):
    try:
        order=Order.objects.get(user=request.user,id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('?')
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            if time_check(order.date_created):
                form.save()
            else:
                return HttpResponse('Time is UP!')
    return render(request,'order.html',{'form':form})