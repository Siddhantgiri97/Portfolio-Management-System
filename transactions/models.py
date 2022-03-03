from django.db import models
from Stocks.models import Stock
from Trader.models import Trader
# Create your models here.


class Transaction(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.stock} -- {self.trader}'
