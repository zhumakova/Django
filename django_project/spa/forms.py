from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['name','age','email','username','password1','password2']