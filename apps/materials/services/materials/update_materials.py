from rest_framework.response import Response
from rest_framework import status
from apps.materials.models import Material
from apps.materials.serializers.materials import MaterialsSerializer

class UpdateMaterialService:
    @staticmethod
    def service(material_id, material_data):
        try:
            material = Material.objects.get(pk=material_id)
        except Material.DoesNotExist:
            return Response(
                {"error": "Material not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MaterialsSerializer(
            material, data=material_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)