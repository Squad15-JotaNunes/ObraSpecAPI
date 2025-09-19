from django.shortcuts import get_object_or_404

from .models import Observation


class ObservationsServices:
    @staticmethod
    def list_all():
        return Observation.objects.all()

    @staticmethod
    def get(pk):
        return get_object_or_404(Observation, pk=pk)

    @staticmethod
    def delete(pk):
        observation = get_object_or_404(Observation, pk=pk)
        observation.delete()
        return True
