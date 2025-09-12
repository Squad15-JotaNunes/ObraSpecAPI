from rest_framework.response import Response
from rest_framework import status

from apps.materials.models import MaterialType
from apps.materials.serializers.material_type import MaterialTypeSerializer


class OneMaterialTypeService:
    @staticmethod
    def service(pk):
        material_type = MaterialType.objects.get(pk=pk)

        if not material_type:
            return Response(
                {"Material Type not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MaterialTypeSerializer(material_type, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
