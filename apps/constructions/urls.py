from django.urls import path
from .views import (
    ConstructionsListAPIView,
    ConstructionsDetailAPIView,
    ConstructionBasedStandardModelsAPIView,
)


urlpatterns = [
    path("", ConstructionsListAPIView.as_view(), name="constructions_list"),
    path(
        "<int:pk>/", ConstructionsDetailAPIView.as_view(), name="constructions_detail"
    ),
    path(
        "using-standard-model/<int:pk>/",
        ConstructionBasedStandardModelsAPIView.as_view(),
        name="construction_based_standard_models",
    ),
]
