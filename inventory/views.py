from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
#import models
from .models import MenuItem, Ingredient, Purchase, RecipeRequirement
# Create your views here.
# def home(request):
#     return render(request, "inventory/home.html")
class Home(TemplateView):#template view for now, later ListView
  template_name = "inventory/home.html"#soon this template gets replaced with balancesheet.html

class BalanceSheet(TemplateView):#template view for now, later ListView
  template_name = "inventory/balancesheet.html"

class Inventory(TemplateView):#template view for now, later ListView
  template_name = "inventory/inventory.html"

class Menu(TemplateView):#template view for now, later ListView
  template_name = "inventory/menu.html"

class Purchases(TemplateView):#template view for now, later ListView
  template_name = "inventory/purchases.html"



# def balancesheet(request):
    # return render(request, "inventory/balancesheet.html")
