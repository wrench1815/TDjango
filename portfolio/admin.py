from django.contrib import admin
from .models import HomeModel, AboutModel


# Register your models here.
@admin.register(HomeModel)
class HomeModelAdmin(admin.ModelAdmin):
    '''Admin View for HomeModel'''


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    '''Admin View for AboutModel'''

    list_display = ('about_head_text', )
