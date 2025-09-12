from django.urls import path

from .views import ObservationsDetailAPIView, ObservationsListAPIView

app_name = "observations"

urlpatterns = [
    # Brands
    path("", ObservationsListAPIView.as_view(), name="observations_list"),
    path("<int:pk>/", ObservationsDetailAPIView.as_view(), name="observations_detail"),
]
