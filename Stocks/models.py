from django.db import models
from Trader.models import Trader
# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=50)
    currentPrice = models.FloatField()
    PreviousPrice = models.FloatField()
    changedPricePercent = models.FloatField()
    trader = models.ManyToManyField(Trader)

    @property
    def get_price(self):
        diff = self.currentPrice - self.PreviousPrice
        return diff

    @property
    def get_percent(self):
        if self.currentPrice > self.PreviousPrice:
            Increase = self.currentPrice - self.PreviousPrice
            percent = Increase / self.PreviousPrice * 100.
        elif self.currentPrice < self.PreviousPrice:
            Decrease = self.currentPrice - self.PreviousPrice
            percent = Decrease / self.PreviousPrice * 100.
        else:
            percent = 0.0
        return percent

    def __str__(self):
        return self.name
