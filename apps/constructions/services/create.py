
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ConstructionSerializer
from ..models import Construction

class CreateConstructionService:
    @staticmethod
    def service(request):
        data = request.data
        serializer = ConstructionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"data": serializer.data}, status=status.HTTP_201_CREATED
        )