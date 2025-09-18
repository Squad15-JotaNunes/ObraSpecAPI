from rest_framework.response import Response
from rest_framework import status
from ..serializers import ConstructionSerializer
from ..models import Construction

class DeleteConstructionService:
    @staticmethod
    def service(pk):
        try:
            construction = Construction.objects.get(pk=pk)
        except Construction.DoesNotExist:
            return Response(
                {"error": "Construction not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        construction.delete()
        return Response(
            {"message": "Construction deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )