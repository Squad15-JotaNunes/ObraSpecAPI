from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.accounts.models import UserPermissions


class UserPermissionsAPIView(APIView):
    """
    API view to retrieve user permissions.
    """

    def get(self, request):
        user = request.user

        if not user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        permissions = get_object_or_404(UserPermissions, user=user)
        return Response(
            {"permissions": permissions.user_type}, status=status.HTTP_200_OK
        )
