from .models import Area, AreaName
from django.shortcuts import get_object_or_404


class AreaNameServices:
    @staticmethod
    def create(data):
        return AreaName.objects.create(**data)

    @staticmethod
    def list_all():
        return AreaName.objects.all()

    @staticmethod
    def delete(pk):
        area_name = get_object_or_404(AreaName, pk=pk)
        area_name.delete()
        return True

    @staticmethod
    def get(pk):
        return get_object_or_404(AreaName, pk=pk)


class AreaServices:
    @staticmethod
    def list_all():
        return Area.objects.all()

    @staticmethod
    def get(pk):
        return get_object_or_404(Area, pk=pk)

    @staticmethod
    def delete(pk):
        area = get_object_or_404(Area, pk=pk)
        area.delete()
        return True
