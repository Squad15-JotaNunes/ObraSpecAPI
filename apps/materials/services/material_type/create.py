from rest_framework.response import Response
from rest_framework import status
from apps.materials.serializers.material_type import MaterialTypeSerializer


class CreateMaterialTypeService:
    @staticmethod
    def service(request):
        data = request.data
        serializer = MaterialTypeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"data": serializer.validated_data}, status=status.HTTP_201_CREATED
        )
