from django.urls import path
from .import views

app_name = 'Trader'

urlpatterns = [
    path('', views.home, name="home"),
    path("profile/<int:pk>/", views.show_user, name="show_user"),
    path("sellStock/<int:pk>/", views.sell_stock, name="sell_stock"),
]
