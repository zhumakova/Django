from django.contrib import admin
from .models import Profile,Order

admin.site.register([Profile,Order])
