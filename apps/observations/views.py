from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import ObservationsServices
from .serializers import ObservationSerializer


class ObservationsListAPIView(APIView):
    # Testado e ok
    def get(self, request):
        observations = ObservationsServices.list_all()
        serializer = ObservationSerializer(observations, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def post(self, request):
        serializer = ObservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


class ObservationsDetailAPIView(APIView):
    # Testado e ok
    def get(self, request, pk):
        observation = ObservationsServices.get(pk)
        serializer = ObservationSerializer(observation)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    # Testado e ok
    def patch(self, request, pk):
        observation = ObservationsServices.get(pk)
        serializer = ObservationSerializer(observation, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    
    # Testado e ok
    def delete(self, request, pk):
        ObservationsServices.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
