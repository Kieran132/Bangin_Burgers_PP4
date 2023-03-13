from . import views
from django.urls import path
from django.views.generic import TemplateView
from order.views import FoodList, SideList, DrinkList


urlpatterns = [
    path('order/', FoodList.as_view(), name='order'),
    path('drinks/', DrinkList.as_view(), name='drink'),
    path('sides/', SideList.as_view(), name='side'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart')
]
