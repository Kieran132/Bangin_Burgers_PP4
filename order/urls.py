from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('order/', views.FoodList.as_view(), name='order')
]