from rest_framework.views import APIView

from .services.create import CreateElementService
from .services.list_all import ListElementService
from .services.get_one import RetrieveElementService
from .services.update import UpdateElementService
from .services.delete import DeleteElementService


class ElementsListAPIView(APIView):
    def get(self, request):
        return ListElementService.service()

    def post(self, request):
        return CreateElementService.service(request)


class ElementsDetailAPIView(APIView):
    def get(self, request, pk):
        return RetrieveElementService.service(pk)

    def patch(self, request, pk):
        return UpdateElementService.service(pk, request.data)

    def delete(self, request, pk):
        return DeleteElementService.service(pk)
