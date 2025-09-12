from rest_framework.response import Response
from rest_framework import status

from ..models import Observation
from ..serializers import ObservationSerializer

class ListAllObservationService:
    @staticmethod
    def service():
        observations = Observation.objects.filter(is_active=True)
        serializer = ObservationSerializer(observations, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)