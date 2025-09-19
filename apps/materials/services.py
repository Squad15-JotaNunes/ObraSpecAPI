from .models import Brand, Material, MaterialType
from django.shortcuts import get_object_or_404


class BrandServices:
    @staticmethod
    def create(data):
        return Brand.objects.create(**data)

    @staticmethod
    def list_all():
        return Brand.objects.all()

    @staticmethod
    def delete(pk):
        brand = get_object_or_404(Brand, pk=pk)
        brand.delete()
        return True

    @staticmethod
    def get(pk):
        return get_object_or_404(Brand, pk=pk)

    @staticmethod
    def get(pk):
        return get_object_or_404(Brand, pk=pk)


class MaterialTypeServices:
    @staticmethod
    def create(data):
        return MaterialType.objects.create(**data)

    @staticmethod
    def list_all():
        return MaterialType.objects.all()

    @staticmethod
    def delete(pk):
        material_type = get_object_or_404(MaterialType, pk=pk)
        material_type.delete()
        return True

    @staticmethod
    def get(pk):
        return get_object_or_404(MaterialType, pk=pk)

    @staticmethod
    def get(pk):
        return get_object_or_404(MaterialType, pk=pk)


class MaterialsServices:
    @staticmethod
    def list_all():
        return Material.objects.all()

    @staticmethod
    def get(pk):
        return get_object_or_404(Material, pk=pk)

    @staticmethod
    def delete(pk):
        material = get_object_or_404(Material, pk=pk)
        material.delete()
        return True
