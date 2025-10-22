from .models import Element, ElementType
from django.shortcuts import get_object_or_404


class ElementTypeServices:
    @staticmethod
    def create(data):
        return ElementType.objects.create(**data)

    @staticmethod
    def list_all():
        return ElementType.objects.all()

    @staticmethod
    def delete(pk):
        element_type = get_object_or_404(ElementType, pk=pk)
        element_type.delete()
        return True

    @staticmethod
    def get(pk):
        return get_object_or_404(ElementType, pk=pk)


class ElementsServices:
    @staticmethod
    def list_all():
        return Element.objects.all()

    @staticmethod
    def get(pk):
        return get_object_or_404(Element, pk=pk)

    @staticmethod
    def delete(pk):
        element = get_object_or_404(Element, pk=pk)
        element.delete()
        return True
