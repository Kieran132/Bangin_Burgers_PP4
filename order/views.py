from django.shortcuts import render
from django.views import generic
from .models import FoodItem


class FoodList(generic.ListView):
    model = FoodItem
    queryset = FoodItem
    template_name = 'order.html'
    paginate_by = 6

