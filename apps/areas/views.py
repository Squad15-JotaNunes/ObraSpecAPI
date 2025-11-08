from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


from .services import AreaNameServices, AreaServices
from apps.areas.serializers import (
    AreaNameSerializer,
    AreaSerializer,
)


class AreaNameListAPIView(APIView):
    def get(self, request):
        area_names = AreaNameServices.list_all()
        serializer = AreaNameSerializer(area_names, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AreaNameSerializer,)
    def post(self, request):
        serializer = AreaNameSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class AreaNameDetailAPIView(APIView):
    def get(self, request, pk):
        area_name = AreaNameServices.get(pk)
        serializer = AreaNameSerializer(area_name)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        area_name = AreaNameServices.get(pk)
        serializer = AreaNameSerializer(area_name, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        AreaNameServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AreaListAPIView(APIView):
    def get(self, request):
        areas = AreaServices.list_all()
        serializer = AreaSerializer(areas, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AreaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class AreaDetailAPIView(APIView):
    def get(self, request, pk):
        area = AreaServices.get(pk)
        serializer = AreaSerializer(area)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        area = AreaServices.get(pk)
        serializer = AreaSerializer(area, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        AreaServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
