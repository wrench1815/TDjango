from django.contrib import admin
from .models import HomeModel

# Register your models here.
@admin.register(HomeModel)
class HomeModelAdmin(admin.ModelAdmin):
    '''Admin View for HomeModel'''
