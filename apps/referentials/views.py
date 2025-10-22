from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ReferentialNameSerializer, ReferentialSerializer
from .services import ReferentialNameServices, ReferentialServices


class ReferentialNameListAPIView(APIView):

    def get(self, request):
        referentials_names = ReferentialNameServices.list_all()
        serializer = ReferentialNameSerializer(referentials_names, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReferentialNameSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class ReferentialNameDetailAPIView(APIView):

    def get(self, request, pk):
        referential_name = ReferentialNameServices.get(pk)
        serializer = ReferentialNameSerializer(referential_name, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        referential_name = ReferentialNameServices.get(pk)
        serializer = ReferentialNameSerializer(
            referential_name, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        ReferentialNameServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReferentialListAPIView(APIView):
    def get(self, request):
        referentials = ReferentialServices.list_all()
        serializer = ReferentialSerializer(referentials, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReferentialSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class ReferentialDetailAPIView(APIView):

    def get(self, request, pk):
        referential = ReferentialServices.get(pk=pk)
        serializer = ReferentialSerializer(referential, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        referential = ReferentialServices.get(pk=pk)
        serializer = ReferentialSerializer(referential, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        ReferentialServices.delete(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
