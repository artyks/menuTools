from django.contrib import admin

from .models import Ingredient
from .models import MenuItem
from .models import Purchase
from .models import RecipeRequirement
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Purchase)
admin.site.register(RecipeRequirement)
