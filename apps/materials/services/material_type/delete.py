from rest_framework.response import Response
from rest_framework import status

from apps.materials.models import MaterialType


class DeleteMaterialTypeService:
    @staticmethod
    def service(pk):
        try:
            material_type = MaterialType.objects.get(pk=pk)
        except MaterialType.DoesNotExist:
            return Response(
                {"detail": "Material Type not found."}, status=status.HTTP_404_NOT_FOUND
            )

        material_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
