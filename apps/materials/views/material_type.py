from rest_framework.views import APIView

from ..services.material_type.all_materials_type import ListAllMaterialTypeService
from ..services.material_type.get_one_material_type import OneMaterialTypeService
from ..services.material_type.create import CreateMaterialTypeService
from ..services.material_type.update_material_type import UpdateMaterialTypeService
from ..services.material_type.delete import DeleteMaterialTypeService


class MaterialTypeListAPIView(APIView):
    def get(self, request):
        return ListAllMaterialTypeService.service()

    def post(self, request):
        return CreateMaterialTypeService.service(request)


class MaterialTypeDetailApiView(APIView):

    def get(self, request, pk):
        return OneMaterialTypeService.service(pk)

    def patch(self, request, pk):
        return UpdateMaterialTypeService.service(pk, request.data)

    def delete(self, request, pk):
        return DeleteMaterialTypeService.service(pk)
