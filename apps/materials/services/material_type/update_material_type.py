from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from apps.materials.models import MaterialType
from apps.materials.serializers.material_type import MaterialTypeSerializer


class UpdateMaterialTypeService:
    @staticmethod
    def service(material_type_id, material_type_data):
        try:
            material_type = MaterialType.objects.get(id=material_type_id)
        except ObjectDoesNotExist:
            raise NotFound("Material Type not found")

        serializer = MaterialTypeSerializer(
            material_type, data=material_type_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
