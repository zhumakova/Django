from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone

def time_check(order_date):
    date_now=timezone.now()
    delta=timezone.timedelta(minutes=5)
    if (date_now-order_date)<=delta:
        return True
    else:
        return False


def incrementOrderCount(profile):
    profile.order_count += 1
    profile.save()

def countMoney(profile, instance):
    price = instance.service.price
    if instance.payment_method == 'wallet':
        if profile.wallet >= price:
            if profile.sale_amount>0:
                price=price-(price*profile.sale_amount)
            profile.wallet -= price
            profile.save()
            instance.status = 'closed'
        else:
            raise ValidationError('no money')

def count_sale(profile):
    if profile.order_count>50:
        profile.sale_amount=0.05
        profile.save()