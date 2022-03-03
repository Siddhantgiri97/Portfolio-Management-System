from django import forms
from .import models



class CreateStock(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = '__all__'
        exclude = ['changedPricePercent', 'trader']
        labels = {
            'name': 'Name',
            'symbol': 'Stock Symbol',
            'currentPrice': 'Price',
            'PreviousPrice': 'Previous Price',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'symbol': forms.TextInput(attrs={'class': 'form-control'}),
            'currentPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'PreviousPrice': forms.TextInput(attrs={'class': 'form-control'}),
        }


