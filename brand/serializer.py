from rest_framework import serializers
from .models import Brand

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')