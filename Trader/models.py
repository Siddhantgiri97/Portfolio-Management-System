from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
