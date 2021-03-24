from rest_framework import serializers
from .models import ProductStore
from product.serializer import ProductSerializer
from brand.serializer import BrandSerializer
from store.serializer import StoreSerializer

class ProductStoreSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()
    brand = BrandSerializer()
    store = StoreSerializer()

    class Meta:
        model = ProductStore
        fields = ('id', 'url','product','brand','store','last_price','last_promotional_price')