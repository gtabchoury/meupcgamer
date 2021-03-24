from django.contrib import admin
from .models import ProductStorePrice
# Register your models here.

class ProductStorePriceAdmin(admin.ModelAdmin):
    list_display = ("product_store","date","price","promotional_price")
    list_filter = ("product_store","date","promotional_price")


admin.site.register(ProductStorePrice, ProductStorePriceAdmin)