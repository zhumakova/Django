from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile
from spa.models import Service
from .forms import OrderForm
from .services import incrementOrderCount,countMoney

def profile_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except (Profile.DoesNotExist,TypeError):
        return HttpResponse('404')
    return render(request,'profile.html',{'profile':profile})


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
    return render(request,'order.html',{'form':form})