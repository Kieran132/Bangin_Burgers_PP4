from django.shortcuts import render
from django.views import generic
from .models import FoodItem, SideItem, DrinkItem


class FoodList(generic.ListView):
    model = FoodItem
    queryset = FoodItem.objects.all()
    template_name = 'order.html'
    paginate_by = 6


class SideList(generic.ListView):
    model = SideItem
    queryset = SideItem.objects.all()
    template_name = 'order.html'
    paginate_by = 6


class DrinkList(generic.ListView):
    model = DrinkItem
    queryset = DrinkItem.objects.all()
    template_name = 'order.html'
    paginate_by = 6


def index(request):
    return render(request, 'index.html')
