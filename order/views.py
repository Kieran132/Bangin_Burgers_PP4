from django.shortcuts import render
from django.views import generic
from .models import FoodItem, SideItem, DrinkItem
from django.views.generic import View


class FoodList(View):
    def get(self, request, *args, **kwargs):
        foods = FoodItem.objects.all()
        context = {
            'foods': foods,
        }
        return render(request, 'order.html', context)


class SideList(View):
    def get(self, request, *args, **kwargs):
        sides = SideItem.objects.all()
        context = {
            'sides': sides,
        }
        return render(request, 'sides.html', context)


class DrinkList(View):
    def get(self, request, *args, **kwargs):
        drink = DrinkItem.objects.all()
        context = {
            'drink': drink,
        }
        return render(request, 'drinks.html', context)


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')
