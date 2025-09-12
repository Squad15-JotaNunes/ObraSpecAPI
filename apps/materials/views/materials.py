from rest_framework.views import APIView

from ..services.materials.all_materials import ListAllMaterialsService
from ..services.materials.get_one_materials import OneMaterialService
from ..services.materials.create import CreateMaterialsService
from ..services.materials.update_materials import UpdateMaterialService
from ..services.materials.delete import DeleteMaterialService


class MaterialsListAPIView(APIView):
    def get(self, request):
        return ListAllMaterialsService.service()

    def post(self, request):
        return CreateMaterialsService.service(request)


class MaterialsDetailApiView(APIView):

    def get(self, request, pk):
        return OneMaterialService.service(pk)

    def patch(self, request, pk):
        return UpdateMaterialService.service(pk, request.data)

    def delete(self, request, pk):
        return DeleteMaterialService.service(pk)
