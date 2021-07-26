from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home.as_view(), name='home'),#this path won't be used after dev. home.html is not a complete page. the actual home page destination is balancesheet.html
    path('balancesheet', views.BalanceSheet.as_view(), name='balancesheet'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('inventory', views.Inventory.as_view(), name='inventory'),
    path('purchases', views.Purchases.as_view(), name='purchases'),
    #===paths for views that edit/create ITEMS
    path('add_menu_item', views.CreateMenuItem.as_view(), name='add_menu_item'),
    path('add_ingredient', views.CreateIngredient.as_view(), name='add_ingredient'),
    path('create_recipe', views.CreateRecipe.as_view(), name='create_recipe'),
    path('create_purchase', views.CreatePurchase.as_view(), name='create_purchase'),
    path('inventory/<pk>/update/', views.UpdateIngredient.as_view(), name='update_ingredient'),
    path('purchase/<pk>/confirm', views.confirmPurchase.as_view(), name='confirm_purchase'),

]
