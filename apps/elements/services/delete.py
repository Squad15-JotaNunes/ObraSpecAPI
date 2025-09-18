from apps.elements.models import Element
from rest_framework.response import Response
from rest_framework import status

class DeleteElementService:
    @staticmethod
    def service(pk):
        try:
            element = Element.objects.get(pk=pk)
            element.delete()
            return Response({'message': 'Element deleted'})
        except Element.DoesNotExist:
            return Response({'error': 'Element not found'}, status=status.HTTP_404_NOT_FOUND)
