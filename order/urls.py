from . import views
from django.urls import path
from django.views.generic import TemplateView
from order.views import FoodList


urlpatterns = [
    path('order/', FoodList.as_view(), name='order'),
    path('', views.index, name='index'),
]
