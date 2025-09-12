from rest_framework.response import Response
from rest_framework import status

from apps.materials.models import MaterialType
from apps.materials.serializers.material_type import MaterialTypeSerializer


class ListAllMaterialTypeService:
    @staticmethod
    def service():
        types_of_materials = MaterialType.objects.all()
        serializer = MaterialTypeSerializer(types_of_materials, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
