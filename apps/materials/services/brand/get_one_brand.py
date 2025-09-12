from rest_framework.response import Response
from rest_framework import status

from apps.materials.models import Brand
from apps.materials.serializers.brand import BrandSerializer


class OneObservationService:
    @staticmethod
    def service(pk):
        brand = Brand.objects.get(pk=pk)

        if not brand:
            return Response({"Brand not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BrandSerializer(brand, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
