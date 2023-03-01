from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('order/', TemplateView.as_view(template_name="order.html")),
]