from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from .services.create import CreateConstructionService
from .services.list_all import ListConstructionService
from .services.get_one import RetrieveConstructionService
from .services.updated import UpdateConstructionService
from .services.delete import DeleteConstructionService


class ConstructionsListAPIView(APIView):
    def get(self, request):
        return ListConstructionService.service()

    def post(self, request):
        return CreateConstructionService.service(request)


class ConstructionsDetailAPIView(APIView):
    def get(self, request, pk):
        return RetrieveConstructionService.service(pk)

    def patch(self, request, pk):
        return UpdateConstructionService.service(pk, request.data)

    def delete(self, request, pk):
        return DeleteConstructionService.service(pk)