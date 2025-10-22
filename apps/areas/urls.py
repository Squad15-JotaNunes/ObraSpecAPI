from django.urls import path

from .views import *

app_name = "areas"

urlpatterns = [
    path("names/", AreaNameListAPIView.as_view(), name="area_name_list"),
    path("names/<int:pk>/", AreaNameDetailAPIView.as_view(), name="area_name_detail"),
    path("", AreaListAPIView.as_view(), name="area_list"),
    path("<int:pk>/", AreaDetailAPIView.as_view(), name="area_detail"),
]
