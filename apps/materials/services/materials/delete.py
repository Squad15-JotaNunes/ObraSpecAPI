from rest_framework.response import Response
from rest_framework import status
from apps.materials.models import Material

class DeleteMaterialService:
    @staticmethod
    def service(pk):
        try:
            material = Material.objects.get(pk=pk)
        except Material.DoesNotExist:
            return Response(
                {"error": "Material not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)