from django.urls import path

from .views import *

app_name = "materials"

urlpatterns = [
    path("brands/", BrandListAPIView.as_view(), name="brand_list"),
    path("brands/<int:pk>/", BrandDetailAPIView.as_view(), name="brand_detail"),
    path(
        "types_of_materials/",
        MaterialTypeListAPIView.as_view(),
        name="materials_type_list",
    ),
    path(
        "types_of_materials/<int:pk>/",
        MaterialTypeDetailApiView.as_view(),
        name="materials_type_detail",
    ),
    path("", MaterialsListAPIView.as_view(), name="materials_list"),
    path("<int:pk>/", MaterialsDetailApiView.as_view(), name="materials_detail"),
]
