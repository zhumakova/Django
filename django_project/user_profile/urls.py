
from django.urls import path
from .views import *
from django.utils import timezone

urlpatterns = [
    path('profile/',profile_page),
    path('order/<int:service_id>/',order_page,name='order'),
    path('order/',my_orders,name='my_orders'),
    path('delete_order/<int:order_id>/',delete_order),
    path('update_order/<int:order_id>/',update_order)
]