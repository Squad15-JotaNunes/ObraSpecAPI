from apps.elements.models import Element
from rest_framework.response import Response
from rest_framework import status

class ElementsServices:
    @staticmethod
    def create(request):
        data = request.data
        element = Element.objects.create(**data)
        return Response({'id': element.id}, status=status.HTTP_201_CREATED)


# Em service não pode ter response
    @staticmethod
    def delete(pk):
        try:
            element = Element.objects.get(pk=pk)
            element.delete()
            return Response({'message': 'Element deleted'})
        except Element.DoesNotExist:
            return Response({'error': 'Element not found'}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def get(pk):
        try:
            element = Element.objects.get(pk=pk)
            return Response({'id': element.id, 'name': element.name})
        except Element.DoesNotExist:
            return Response({'error': 'Element not found'}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def list():
        elements = Element.objects.all().values()
        return Response(list(elements))

    @staticmethod
    def update(pk, data):
        try:
            element = Element.objects.get(pk=pk)
            for key, value in data.items():
                setattr(element, key, value)
            element.save()
            return Response({'id': element.id})
        except Element.DoesNotExist:
            return Response({'error': 'Element not found'}, status=status.HTTP_404_NOT_FOUND)
