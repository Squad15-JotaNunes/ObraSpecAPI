from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from apps.materials.models import Brand
from apps.materials.serializers.brand import BrandSerializer


class UpdatedObservationService:
    @staticmethod
    def service(brand_id, brand_data):
        try:
            brand = Brand.objects.get(id=brand_id)
        except ObjectDoesNotExist:
            raise NotFound("Observation not found")

        serializer = BrandSerializer(brand, data=brand_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
