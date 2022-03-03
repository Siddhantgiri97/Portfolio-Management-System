from django.urls import path
from .import views
app_name = 'Stocks'

urlpatterns = [
    path('', views.home, name="home"),
    path('stocksList/', views.stocksList, name="stocksList"),
    path('stockCreate/', views.stock_create, name="stock_create"),
    path('stockDetails/<int:pk>/', views.stockDetails, name="stockDetails"),
    path('stockUpdate/<int:pk>/', views.stock_update, name="stock_update"),
    path('buyStock/', views.buy_stock, name="buy_stock"),
    path('stockDelete/<int:pk>/', views.stock_delete, name="stock_delete"),
    path("searchStock/", views.search_stock, name="search_stock"),
]
