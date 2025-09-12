from rest_framework.response import Response
from rest_framework import status
from apps.materials.serializers.materials import MaterialsSerializer


class CreateMaterialsService:
    @staticmethod
    def service(request):
        data = request.data

        serializer = MaterialsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
