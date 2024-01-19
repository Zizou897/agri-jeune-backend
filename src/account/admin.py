from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.

from .models import Store

@admin.register(Store)
class Store(admin.ModelAdmin):
    list_display = ('logo','name', 'address', 'phone_number', 'user')
    search_fields = ['name']


    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"
