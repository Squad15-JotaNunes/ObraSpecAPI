from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .services import ElementTypeServices, ElementsServices
from apps.elements.serializers import (
    ElementTypeSerializer,
    ElementSerializer,
)


class ElementTypeListAPIView(APIView):
    def get(self, request):
        element_types = ElementTypeServices.list_all()
        serializer = ElementTypeSerializer(element_types, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ElementTypeSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class ElementTypeDetailAPIView(APIView):
    def get(self, request, pk):
        element_type = ElementTypeServices.get(pk)
        serializer = ElementTypeSerializer(element_type)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        element_type = ElementTypeServices.get(pk)
        serializer = ElementTypeSerializer(
            element_type, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        ElementTypeServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ElementsListAPIView(APIView):
    def get(self, request):
        elements = ElementsServices.list_all()
        serializer = ElementSerializer(elements, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ElementSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class ElementsDetailAPIView(APIView):
    def get(self, request, pk):
        element = ElementsServices.get(pk)
        serializer = ElementSerializer(element)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        element = ElementsServices.get(pk)
        serializer = ElementSerializer(element, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        ElementsServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
