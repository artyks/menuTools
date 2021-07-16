from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.
# def home(request):
#     return render(request, "inventory/home.html")
class Home(TemplateView):
  template_name = "inventory/home.html"#soon this template gets replaced with balancesheet.html


    # return context
def balancesheet(request):
    return render(request, "inventory/balancesheet.html")
