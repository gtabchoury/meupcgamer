from django.urls import path

from .views import ProductAPIView

urlpatterns = [
    path('category/<str:category_id>', ProductAPIView.as_view(), name='Get products by category_id'),
]