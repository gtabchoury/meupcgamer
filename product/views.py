from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from category.models import Category
from .serializer import ProductSerializer
from rest_framework import status, authentication, exceptions

# Create your views here.

class ProductAPIView(APIView):
    def get(self, request, category_id=None):
        try:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return Response({'error': 'Categoria não encontrada'}, status=status.HTTP_404_NOT_FOUND)

            products = Product.objects.filter(category=category)

            return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Interal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
