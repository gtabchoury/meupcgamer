from rest_framework import serializers
from .models import Product
from category.serializer import CategorySerializer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'name','category')