from django.contrib import admin

# Register your models here.


from .models import Sectors, PaymentMethod, Measure, ProductCategory


@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ('name', 'slug','language_key', 'created_at', 'publish')
    search_fields = ['name']




@admin.register(Measure)
class Measure(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'language_key', 'created_at')
    search_fields = ['name']


@admin.register(PaymentMethod)
class PaymentMethod(admin.ModelAdmin):
    list_display = ('name', 'language_key', 'created_at')
    search_fields = ['name']



@admin.register(Sectors)
class Sectors(admin.ModelAdmin):
    list_display = ('name', 'language_key', 'created_at')
    search_fields = ['name']
