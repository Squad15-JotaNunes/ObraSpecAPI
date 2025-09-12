from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from ..models import Observation
from ..serializers import ObservationSerializer


class UpdatedObservation:
    @staticmethod
    def service(observation_id, observation_data):
        try:
            observation = Observation.objects.get(id=observation_id)
        except ObjectDoesNotExist:
            raise NotFound("Observation not found")

        serializer = ObservationSerializer(
            observation, data=observation_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
