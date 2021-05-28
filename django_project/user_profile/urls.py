from django.urls import path
from .views import *


urlpatterns = [
    path('profile/', profile_page),
    path('order/<int:service_id>', order_page,name='order'),
]