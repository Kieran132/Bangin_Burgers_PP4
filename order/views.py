from django.shortcuts import render
from django.views import generic
from .models import FoodItem, FoodTest


class FoodList(generic.ListView):
    model = FoodItem
    queryset = FoodItem.objects.all()
    template_name = 'order.html'
    paginate_by = 6


class FoodList(generic.ListView):
    model = FoodTest
    queryset = FoodTest.objects.all()
    template_name = 'order.html'
    paginate_by = 6


