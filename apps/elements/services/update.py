from apps.elements.models import Element
from rest_framework.response import Response
from rest_framework import status

class UpdateElementService:
    @staticmethod
    def service(pk, data):
        try:
            element = Element.objects.get(pk=pk)
            for key, value in data.items():
                setattr(element, key, value)
            element.save()
            return Response({'id': element.id})
        except Element.DoesNotExist:
            return Response({'error': 'Element not found'}, status=status.HTTP_404_NOT_FOUND)
