from apps.elements.models import Element
from rest_framework.response import Response

class ListElementService:
    @staticmethod
    def service():
        elements = Element.objects.all().values()
        return Response(list(elements))
