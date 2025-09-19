from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .services import BrandServices, MaterialsServices, MaterialTypeServices
from apps.materials.serializers import (
    BrandSerializer,
    MaterialTypeSerializer,
    MaterialsSerializer,
)


class BrandListAPIView(APIView):
    # Testado e ok
    def get(self, request):
        brands = BrandServices.list_all()
        serializer = BrandSerializer(brands, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # cria o objeto
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class BrandDetailAPIView(APIView):
    # Testado e ok
    def get(self, request, pk):
        brand = BrandServices.get(pk)
        serializer = BrandSerializer(brand)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def patch(self, request, pk):
        brand = BrandServices.get(pk)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def delete(self, request, pk):
        BrandServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MaterialTypeListAPIView(APIView):
    # Testado e ok
    def get(self, request):
        types_materials = MaterialTypeServices.list_all()
        serializer = MaterialTypeSerializer(types_materials, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def post(self, request):
        serializer = MaterialTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class MaterialTypeDetailApiView(APIView):
    # Testado e ok
    def get(self, request, pk):
        material_type = MaterialTypeServices.get(pk)
        serializer = MaterialTypeSerializer(material_type)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def patch(self, request, pk):
        material_type = MaterialTypeServices.get(pk)
        serializer = MaterialTypeSerializer(
            material_type, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def delete(self, request, pk):
        MaterialTypeServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MaterialsListAPIView(APIView):
    # Testado e ok
    def get(self, request):
        materials = MaterialsServices.list_all()
        serializer = MaterialsSerializer(materials, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def post(self, request):
        serializer = MaterialsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class MaterialsDetailApiView(APIView):
    # Testado e ok
    def get(self, request, pk):
        material = MaterialsServices.get(pk)
        serializer = MaterialsSerializer(material)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def patch(self, request, pk):
        material = MaterialsServices.get(pk)
        serializer = MaterialsSerializer(material, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def delete(self, request, pk):
        MaterialsServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
