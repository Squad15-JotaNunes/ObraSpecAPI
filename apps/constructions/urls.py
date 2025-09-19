from django.urls import path
from .views import ConstructionsListAPIView, ConstructionsDetailAPIView

app_name = "constructions"

urlpatterns = [
    path("", ConstructionsListAPIView.as_view(), name="constructions_list"),
    path("<int:pk>/", ConstructionsDetailAPIView.as_view(), name="constructions_detail"),
]
