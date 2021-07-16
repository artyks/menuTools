from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("balancesheet", views.balancesheet, name="balancesheet"),
]
