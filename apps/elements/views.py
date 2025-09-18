from rest_framework.views import APIView

from .services.services import ElementsServices


class ElementsListAPIView(APIView):
    def get(self, request):
        return ElementsServices.list()

    def post(self, request):
        return ElementsServices.create(request)


class ElementsDetailAPIView(APIView):
    def get(self, request, pk):
        return ElementsServices.get(pk)

    def patch(self, request, pk):
        return ElementsServices.update(pk, request.data)

    def delete(self, request, pk):
        return ElementsServices.delete(pk)
