from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerializer
from rest_framework import status, authentication, exceptions

# Create your views here.

class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.filter().order_by('order')

        print(categories)

        return Response(CategorySerializer(categories, many=True).data, status=status.HTTP_200_OK)
        
