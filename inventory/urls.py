from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),#function-based, for dev only. delete eventually
    path('', views.Home.as_view(), name='home'),#this path won't be used after dev. home.html is not a complete page. the actual home page destination is balancesheet.html
    path("balancesheet", views.balancesheet, name="balancesheet"),#after all pages are running, this is the home page, served only after a successful login
]
