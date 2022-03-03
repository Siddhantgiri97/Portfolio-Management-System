from django import forms
from .import models


class BuyStock(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = '__all__'
        labels = {
            'stock': 'Stock',
            "trader": "Trader"
        }
        widgets = {
            'stock': forms.Select(attrs={'class': 'form-control'}),
            'trader': forms.Select(attrs={'class': 'form-control'}),
        }
