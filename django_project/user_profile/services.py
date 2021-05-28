from django.core.exceptions import ValidationError

def incrementOrderCount(profile):
    profile.order_count += 1
    profile.save()

def countMoney(profile, instance):
    price = instance.service.price
    if instance.payment_method == 'wallet':
        if profile.wallet >= price:
            profile.wallet -= price
            profile.save()
            instance.status = 'closed'
        else:
            raise ValidationError('no money')