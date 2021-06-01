from django.urls import path
from .views import *

urlpatterns = [
    path('card_create/',cardCreate),
    path('increment/',incrementBalance),
    path('transaction/',transactionPage),
]