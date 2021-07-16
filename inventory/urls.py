from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),#function-based, for dev only. delete eventually
    path('', views.Home.as_view(), name='home'),#this path won't be used after dev. home.html is not a complete page. the actual home page destination is balancesheet.html
    path('balancesheet', views.BalanceSheet.as_view(), name='balancesheet'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('inventory', views.Inventory.as_view(), name='inventory'),
    path('purchases', views.Purchases.as_view(), name='purchases'),
]
