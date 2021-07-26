from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin#for class views, add parameter to function call
from django.contrib.auth.decorators import login_required#for function views. prepend function def with @login_required on line above
from django.contrib.auth import logout
# from django.urls import reverse_lazy

#import models
from .models import MenuItem, Ingredient, Purchase, RecipeRequirement
#import forms
from .forms import  IngredientForm, MenuItemForm, PurchaseForm, RecipeRequirementForm, IngredientUpdateForm
# Create your views here.
#i guessi dont need this view=======
# def login_view(request):
#     context = {
#     "login_view": "active"
#     }
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("balancesheet")#VERIFY
#         else:
#             return HttpResponse("invalid credentials")
#     return render(request, "registration/login.html", context)
#===========
class Home(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"#soon this template gets replaced with balancesheet.html


class BalanceSheet(LoginRequiredMixin, TemplateView):
    template_name = "inventory/balancesheet.html"

    @property#calculate total cost of all ingredients in all items sold
    def total_purchases_cost(self):
        total_cost = 0.0
        all_PO = Purchase.objects.all()
        for this_PO in all_PO:
            total_cost += this_PO.menuitem.sum_recipe_prices()
        return total_cost

    @property#calculate total price off all menu items sold
    def total_sales_price(self):
        total_price = 0.0
        all_PO = Purchase.objects.all()
        for this_PO in all_PO:
            total_price += this_PO.menuitem.price
        return total_price

    def get_context_data(self):
        context = super().get_context_data()
        context["totalcost"] = self.total_purchases_cost
        context["totalsales"] = self.total_sales_price
        context["profitorloss"] = self.total_sales_price - self.total_purchases_cost
        return context

class Inventory(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/inventory.html"

class Menu(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["recreqs"] = RecipeRequirement.objects.all()
        context["menuitems"] = MenuItem.objects.all()
        context["ingredients"] = Ingredient.objects.all()
        # context["pricesum"] = self.sum_recipe_prices()
        return context


class Purchases(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.all()
        return context
#===CLASSES FOR ADDING OR UPDATING ITEMS, BASED ON FORMS===


class CreateMenuItem(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemForm
class CreateIngredient(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm
class UpdateIngredient(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientUpdateForm

class CreateRecipe(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/create_recipe.html"
    form_class = RecipeRequirementForm

class CreatePurchase(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/create_purchase.html"
    form_class = PurchaseForm

class confirmPurchase(LoginRequiredMixin, ListView):
    template_name = "inventory/confirm_purchase.html"
    model = Purchase
    # thisPO = Purchase.objects.get(id=self.kwargs['pk'])
    def get_context_data(self):
        context = super().get_context_data()
        context["purchase"] = Purchase.objects.get(id=self.kwargs['pk'])
        context["depleteinventory"] = self.deplete_inventory
        return context
    @property
    def deplete_inventory(self):
        thisPI = Purchase.objects.get(id=self.kwargs['pk'])
        rrSet = thisPI.menuitem.reciperequirement_set.all()
        for thisRR in rrSet:
            thisINname = thisRR.ingredient.name
            thisQTY = thisRR.quantity
            ING_TAR = Ingredient.objects.get(name=thisINname)
            ING_TAR.availableQuantity -= thisQTY
            ING_TAR.save()

def logout_view(request):
  logout(request)
  return redirect("balancesheet")#VERIFY maybe it redirects to "home"
