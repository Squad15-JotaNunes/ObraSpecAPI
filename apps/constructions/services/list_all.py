from rest_framework.response import Response
from rest_framework import status
from ..serializers import ConstructionSerializer
from ..models import Construction


class ListConstructionService:
    @staticmethod
    def service():
        constructions = Construction.objects.all()
        serializer = ConstructionSerializer(constructions, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)