from django.shortcuts import render
from django.views import generic
from .models import FoodItem, FoodTest


class FoodList(generic.ListView):
    model = FoodItem
    queryset = FoodItem.objects.all()
    template_name = 'order.html'
    paginate_by = 6


