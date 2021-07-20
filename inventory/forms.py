from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class IngredientUpdateForm(forms.ModelForm):
    disabled_fields = ('name',)

    class Meta:
        model = Ingredient
        fields = ["name", "availableQuantity"]

    def __init__(self, *args, **kwargs):
        super(IngredientUpdateForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True
