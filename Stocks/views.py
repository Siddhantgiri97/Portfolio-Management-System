from django.shortcuts import render, redirect
from .models import Stock
from .forms import CreateStock
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from transactions.forms import BuyStock
from Trader.models import Trader
# Create your views here.


def home(request):
    return render(request, "Stocks/home.html")


@login_required(login_url="/accounts/login/")
def stocksList(request):
    stocks = Stock.objects.all()
    return render(request, 'Stocks/stocks_list.html', {'stocks': stocks})


@login_required(login_url="/accounts/login/")
def stockDetails(request, pk):
    stock = Stock.objects.get(id=pk)
    return render(request, 'Stocks/stock_details.html', {'stock': stock})


@login_required(login_url="/accounts/login/")
def stock_create(request):
    if request.method == 'POST':
        form = CreateStock(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Stocks:stocksList')
    else:
        form = CreateStock()
    return render(request, 'Stocks/stock_create.html', {'form': form})


@login_required(login_url="/accounts/login/")
def stock_update(request, pk):
    stock = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateStock(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('Stocks:stocksList')
    else:
        form = CreateStock(instance=stock)
    return render(request, 'Stocks/stock_update.html', {'form': form})


@login_required(login_url="/accounts/login/")
def buy_stock(request):
    if request.method == 'POST':
        form = BuyStock(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Stocks:stocksList')
    else:
        form = BuyStock()
    return render(request, 'Stocks/buy_stock.html', {'form': form})


@login_required(login_url="/accounts/login/")
def stock_delete(request, pk):
    stock = Stock.objects.get(id=pk)
    stock.delete()
    return redirect('Stocks:stocksList')


@login_required(login_url="/accounts/login/")
def search_stock(request):
    query = request.GET.get('search')
    results = Stock.objects.filter(
        Q(name__icontains=query))
    # Pagination
    context = {'results': results, 'query': query}
    return render(request, 'Stocks/search.html', context)
