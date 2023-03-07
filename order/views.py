from django.shortcuts import render
from django.views import generic
from .models import FoodItem, SideItem, DrinkItem
from django.views.generic import View


class FoodList(View):
    def get(self, request, *args, **kwargs):
        foods = FoodItem.objects.all()
        drinks = DrinkItem.objects.all()
        sides = SideItem.objects.all()
        context = {
            'foods': foods,
            'drinks': drinks,
            'sides': sides,
        }
        return render(request, 'order.html', context)


def index(request):
    return render(request, 'index.html')
