from rest_framework.response import Response
from rest_framework import status

from ..models import Observation
from ..serializers import ObservationSerializer


class OneObservationService:
    @staticmethod
    def service(pk):
        observation = Observation.objects.get(pk=pk)

        if not observation:
            return Response({"Observation not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ObservationSerializer(observation, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
