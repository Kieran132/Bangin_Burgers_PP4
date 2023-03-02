from django.contrib import admin
from .models import FoodItem, SideItem, DrinkItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name', )}
    summernote_fields = ('description')


@admin.register(SideItem)
class FoodAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name', )}
    summernote_fields = ('description')


@admin.register(DrinkItem)
class FoodAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name', )}
    summernote_fields = ('description')
