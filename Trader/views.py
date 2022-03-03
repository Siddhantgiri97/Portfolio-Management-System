from django.shortcuts import render, redirect
from .models import Trader
from Stocks.models import Stock
from transactions.models import Transaction
# Create your views here.


def home(request):
    return render(request, "Trader/home.html")


def show_user(request, pk):
    trader = Trader.objects.get(id=pk)
    trader_stocks = trader.transaction_set.all()
    context = {'trader': trader, 'trader_stocks': trader_stocks}
    return render(request, "Trader/profile.html", context)


def sell_stock(request, pk):
    transaction = Transaction.objects.get(id=pk)
    transaction.delete()
    return redirect('Stocks:stocksList')
