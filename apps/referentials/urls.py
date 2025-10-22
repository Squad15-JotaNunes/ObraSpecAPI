from django.urls import path

from .views import (
    ReferentialNameListAPIView,
    ReferentialNameDetailAPIView,
    ReferentialListAPIView,
    ReferentialDetailAPIView,
)

app_name = "referentials"

urlpatterns = [
    path("", ReferentialListAPIView.as_view(), name="referential_list"),
    path("<int:pk>/", ReferentialDetailAPIView.as_view(), name="referential_detail"),
    path("name/", ReferentialNameListAPIView.as_view(), name="referential_name_list"),
    path(
        "name/<int:pk>/",
        ReferentialNameDetailAPIView.as_view(),
        name="referential_name_detail",
    ),
]
