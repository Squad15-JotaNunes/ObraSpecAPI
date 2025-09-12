from rest_framework.views import APIView

from ..services.brand.create import CreateBrandService
from ..services.brand.all_brands import ListAllBrandsService
from ..services.brand.update_brand import UpdatedObservationService
from ..services.brand.get_one_brand import OneObservationService
from ..services.brand.delete import DeleteBrandService


class BrandListAPIView(APIView):
    def get(self, request):
        return ListAllBrandsService.service()

    def post(self, request):
        return CreateBrandService.service(request)


class BrandDetailAPIView(APIView):
    def get(self, request, pk):
        return OneObservationService.service(pk)

    def patch(self, request, pk):
        return UpdatedObservationService.service(pk, request.data)

    def delete(self, request, pk):
        return DeleteBrandService.service(pk)
