from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from .views import PriceAPIView

urlpatterns = [
    path('products/', include('product.urls')),
    path('categories/', include('category.urls')),
    path('product-prices/', PriceAPIView.as_view()),
    path('admin/', admin.site.urls),
]