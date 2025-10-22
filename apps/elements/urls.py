from django.urls import path

from .views import *

app_name = "elements"

urlpatterns = [
    path("types/", ElementTypeListAPIView.as_view(), name="element_type_list"),
    path(
        "types/<int:pk>/",
        ElementTypeDetailAPIView.as_view(),
        name="element_type_detail",
    ),
    path("", ElementsListAPIView.as_view(), name="elements_list"),
    path("<int:pk>/", ElementsDetailAPIView.as_view(), name="elements_detail"),
]
