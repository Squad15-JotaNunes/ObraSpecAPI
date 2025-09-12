from rest_framework.response import Response
from rest_framework import status

from ..models import Observation


class DeleteObservationService:
    @staticmethod
    def service(pk):
        try:
            observation = Observation.objects.get(pk=pk)
        except Observation.DoesNotExist:
            return Response(
                {"detail": "Observation not found."}, status=status.HTTP_404_NOT_FOUND
            )

        observation.is_active = False
        observation.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
