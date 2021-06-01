from django.db import models
from user_profile.models import Profile


class Card(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    code = models.IntegerField()
    cvv = models.IntegerField()
    balance = models.PositiveIntegerField(default=0)


class Transaction(models.Model):
    from_profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,
                                     null=True,related_name='transaction_from')
    to_profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,
                                   null=True,related_name='transaction_to')
    date_created = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=0)


