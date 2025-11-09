from django.urls import path
from apps.documents.views import DocumentsDetailAPIView

urlpatterns = [
    path("<int:pk>/", DocumentsDetailAPIView.as_view(), name="documents-detail"),
]
