from django.db import models


class Service(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    master=models.ForeignKey('Master',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class Master(models.Model):
    photo=models.ImageField()
    full_name=models.CharField(max_length=30)
    exp=models.IntegerField(default=0)
    birth_date=models.DateField()

    def __str__(self):
        return self.full_name