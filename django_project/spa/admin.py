from django.contrib import admin
from .models import Service,Master,Certificates
admin.site.register([Service,Master,Certificates])
