from django import forms
from .models import Card,Transaction


class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['profile', 'code', 'cvv']


class PayForm(forms.Form):
    amount = forms.IntegerField(min_value=20,max_value=50000)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['to_profile','amount']