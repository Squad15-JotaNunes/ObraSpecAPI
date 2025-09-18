from django.urls import path
from .views import ElementsListAPIView, ElementsDetailAPIView

urlpatterns = [
    path('elements/', ElementsListAPIView.as_view(), name='elements-list'),
    path('elements/<int:pk>/', ElementsDetailAPIView.as_view(), name='elements-detail'),
]
