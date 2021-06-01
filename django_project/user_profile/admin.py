from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','service','status','payment_method','date_created']
    readonly_fields = ['date_created']
admin.site.register(Order,OrderAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo','name','age','email','order_count','wallet']
    readonly_fields = ['order_count','wallet']

admin.site.register(Profile,ProfileAdmin)

