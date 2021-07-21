from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
#import models
from .models import MenuItem, Ingredient, Purchase, RecipeRequirement
#import forms
from .forms import  IngredientForm, MenuItemForm, PurchaseForm, RecipeRequirementForm, IngredientUpdateForm
# Create your views here.
# def home(request):
#     return render(request, "inventory/home.html")
class Home(TemplateView):
    template_name = "inventory/home.html"#soon this template gets replaced with balancesheet.html

class BalanceSheet(TemplateView):#template view for now, later ListView
    template_name = "inventory/balancesheet.html"

class Inventory(ListView):
    model = Ingredient
    template_name = "inventory/inventory.html"

class Menu(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


    def get_context_data(self):
        context = super().get_context_data()
        context["recreqs"] = RecipeRequirement.objects.all()
        context["menuitems"] = MenuItem.objects.all()
        context["ingredients"] = Ingredient.objects.all()
        # context["ing_price"] = RecipeRequirement.calculate_price()
        return context
class Purchases(TemplateView):#template view for now, later ListView
    template_name = "inventory/purchases.html"


#===CLASSES FOR ADDING OR UPDATING ITEMS, BASED ON FORMS===


class CreateMenuItem(CreateView):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemForm
class CreateIngredient(CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm
class UpdateIngredient(UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientUpdateForm

class CreateRecipe(CreateView):
    model = RecipeRequirement
    template_name = "inventory/create_recipe.html"
    form_class = RecipeRequirementForm
