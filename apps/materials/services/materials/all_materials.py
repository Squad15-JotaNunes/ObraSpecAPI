from rest_framework.response import Response
from apps.materials.serializers.materials import MaterialsSerializer
from apps.materials.models import Material


class ListAllMaterialsService:
    @staticmethod
    def service():
        materials = Material.objects.all()
        serializer = MaterialsSerializer(materials, many=True)
        return Response({"data": serializer.data})
