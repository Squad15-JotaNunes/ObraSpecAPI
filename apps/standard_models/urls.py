from django.urls import path
from .views import StandardModelListAPIView, StandardModelDetailAPIView

app_name = "standard_model"

urlpatterns = [
    path("", StandardModelListAPIView.as_view(), name="standard_model_list"),
    path("<int:pk>/", StandardModelDetailAPIView.as_view(), name="standard_model_detail"),
]
