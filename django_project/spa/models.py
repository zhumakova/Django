from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=40,unique=True)
    price = models.IntegerField()
    master = models.ForeignKey("Master",on_delete=models.SET_NULL,null=True,related_name="services")


    def __str__(self):
        return self.name

class Master(models.Model):
    photo = models.ImageField()
    full_name = models.CharField(max_length=30)
    exp = models.IntegerField(default=0)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name

class Certificates(models.Model):
    name=models.CharField(max_length=40)
    date_graduate=models.DateField()
    date_expired=models.DateField()
    school=models.CharField(max_length=40)
    photo=models.ImageField()
    status=models.CharField(max_length=40,choices=(
        ('active','active'),
        ('dead','dead')
    ),default='active')
    master=models.ForeignKey(Master,on_delete=models.CASCADE)
