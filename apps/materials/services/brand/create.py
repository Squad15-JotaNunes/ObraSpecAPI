from rest_framework.response import Response
from rest_framework import status
from apps.materials.serializers.brand import BrandSerializer


class CreateBrandService:
    @staticmethod
    def service(request):
        data = request.data
        serializer = BrandSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"data": serializer.validated_data}, status=status.HTTP_201_CREATED
        )
