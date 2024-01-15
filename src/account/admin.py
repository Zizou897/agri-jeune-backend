from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.

from .models import Store

@admin.register(Store)
class Store(admin.ModelAdmin):
    list_display = ('logo','name', 'address', 'phone_number', 'user')
    search_fields = ['name']

