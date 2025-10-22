from rest_framework.response import Response
from rest_framework import status
from ..serializers import ConstructionSerializer
from ..models import Construction


class ConstructionService:
    @staticmethod
    def store(data):
        return Construction.objects.create(**data)  # desempacota o dict

    @staticmethod
    def show(pk):
        return Construction.objects.get(pk=pk)

    @staticmethod
    def index():
        return Construction.objects.all()

    @staticmethod
    def update(pk, validated_data):
        construction = Construction.objects.get(pk=pk)
        serializer = ConstructionSerializer(
            construction, data=validated_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer

    @staticmethod
    def destroy(pk):
        construction = Construction.objects.get(pk=pk)
        construction.delete()
        return True
