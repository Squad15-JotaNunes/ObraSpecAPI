from rest_framework.views import APIView

from .services.create import CreateObservationService
from .services.list_all_observations import ListAllObservationService
from .services.get_one_observation import OneObservationService
from .services.updated_observation import UpdatedObservation
from .services.delete import DeleteObservationService

class ObservationsListAPIView(APIView):
    def get(self, request):
        return ListAllObservationService.service()

    def post(self, request):
        return CreateObservationService.service(request)


class ObservationsDetailAPIView(APIView):

    def get(self, request, pk):
        return OneObservationService.service(pk)

    def patch(self, request, pk):
        return UpdatedObservation.service(pk, request.data)

    def delete(self, request, pk):
        return DeleteObservationService.service(pk)