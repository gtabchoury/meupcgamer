from django.contrib import admin
from .models import ProductStore
# Register your models here.

class ProductStoreAdmin(admin.ModelAdmin):
    list_display = ("product","brand","store","url")
    list_filter = ("product","brand","store","url")


admin.site.register(ProductStore, ProductStoreAdmin)