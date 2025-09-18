from rest_framework.response import Response
from rest_framework import status
from ..serializers import ConstructionSerializer
from ..models import Construction


class UpdateConstructionService:
    @staticmethod
    def service(request, pk):
        try:
            construction = Construction.objects.get(pk=pk)
        except Construction.DoesNotExist:
            return Response(
                {"error": "Construction not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ConstructionSerializer(construction, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data}, status=status.HTTP_200_OK)