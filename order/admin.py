from django.contrib import admin
from .models import FoodItem, FoodTest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name', )}
    summernote_fields = ('description')


@admin.register(FoodTest)
class Testing(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name', )}
    summernote_fields = ('description')

