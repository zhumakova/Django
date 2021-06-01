from django.shortcuts import render
from .forms import CardCreateForm,PayForm,TransactionForm
from .models import Card

def cardCreate(request):
    form = CardCreateForm(initial={'profile':request.user.profile})
    if request.method == 'POST':
        form = CardCreateForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'card_form.html',{'form':form})

def incrementBalance(request):
    form = PayForm()
    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            profile = request.user.profile
            card = Card.objects.get(profile=profile)
            if card.balance >= amount:
                card.balance -= amount
                profile.wallet += amount
                card.save()
                profile.save()
    return render(request,'pay_form.html',{'form':form})

def transactionPage(request):
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            from_profile = request.user.profile
            to_profile = form.instance.to_profile
            amount = form.instance.amount
            print(from_profile is not to_profile)
            if from_profile != to_profile:
               if from_profile.wallet >= amount:
                    from_profile.wallet -= amount
                    to_profile.wallet += amount
                    from_profile.save()
                    to_profile.save()
                    form.instance.from_profile = from_profile
                    form.save()
    return render(request,'transaction_form.html',{'form':form})