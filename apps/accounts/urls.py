from django.urls import path
from apps.accounts.views import UserPermissionsAPIView

urlpatterns = [
    path("user-permitions/", UserPermissionsAPIView.as_view(), name="user_permissions")
]
