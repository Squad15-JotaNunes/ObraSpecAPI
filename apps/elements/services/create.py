from apps.elements.models import Element
from rest_framework.response import Response
from rest_framework import status

class CreateElementService:
    @staticmethod
    def service(request):
        data = request.data
        element = Element.objects.create(**data)
        return Response({'id': element.id}, status=status.HTTP_201_CREATED)
