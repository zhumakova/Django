from django.contrib.auth.models import User
from django.db import models
from spa.models import Service
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField()
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField()
    wallet=models.PositiveIntegerField()
    order_count=models.PositiveIntegerField(default=0)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    service=models.ForeignKey(Service,on_delete=models.SET_NULL,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=(
        ('in_process','in_process'),
        ('closed','closed')
    ),max_length=15,default='in_process')