from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    master=models.CharField(max_length=30)