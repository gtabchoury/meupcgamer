from rest_framework import serializers
from .models import ProductStorePrice
from product_store.serializer import ProductStoreSerializer

class ProductStorePriceSerializer(serializers.HyperlinkedModelSerializer):
    product_store = ProductStoreSerializer()

    class Meta:
        model = ProductStorePrice
        fields = ('id', 'date','product_store','price','promotional_price')