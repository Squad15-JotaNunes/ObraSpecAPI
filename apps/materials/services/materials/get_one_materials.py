from rest_framework.response import Response
from rest_framework import status
from apps.materials.models import Material
from apps.materials.serializers.materials import MaterialsSerializer


class OneMaterialService:
    @staticmethod
    def service(pk):
        try:
            material = Material.objects.get(pk=pk)
        except Material.DoesNotExist:
            return Response(
                {"error": "Material not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MaterialsSerializer(material, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
