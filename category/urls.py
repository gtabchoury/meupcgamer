from django.urls import path

from .views import CategoryAPIView

urlpatterns = [
    path('all/', CategoryAPIView.as_view(), name='Get all categories'),
]