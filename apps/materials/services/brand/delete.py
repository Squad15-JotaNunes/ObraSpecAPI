from rest_framework.response import Response
from rest_framework import status

from apps.materials.models import Brand


class DeleteBrandService:
    @staticmethod
    def service(pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(
                {"detail": "Brand not found."}, status=status.HTTP_404_NOT_FOUND
            )

        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
