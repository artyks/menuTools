from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=20)
  unit = models.CharField(max_length=20, default="oz")
  availableQuantity = models.IntegerField(default=10)
  unitPrice = models.FloatField(default=1.50)

  def __str__(self):
    return self.name

class MenuItem(models.Model):
  title = models.CharField(max_length=20)
  price = models.FloatField(default=11.50)

  def __str__(self):
    return self.name

class Purchase(models.Model):
  date = models.DateTimeField(auto_now=True)
  menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

class RecipeRequirement(models.Model):
  menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
