from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'service','payment_method']

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['photo','name','age','email']