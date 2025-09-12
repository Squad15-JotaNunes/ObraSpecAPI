from rest_framework.response import Response
from rest_framework import status

from apps.materials.models import Brand
from apps.materials.serializers.brand import BrandSerializer


class ListAllBrandsService:
    @staticmethod
    def service():
        observations = Brand.objects.all()
        serializer = BrandSerializer(observations, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
