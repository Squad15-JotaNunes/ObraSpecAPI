from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConstructionSerializer
from .services.construction_service import ConstructionService
from apps.constructions.models import Construction
from apps.standard_models.models import StandardModel
from django.shortcuts import get_object_or_404


class ConstructionsListAPIView(APIView):
    def get(self, request):
        try:
            constructions = ConstructionService.index()
            serializer = ConstructionSerializer(constructions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            construction = ConstructionService.store(request.data)
            serializer = ConstructionSerializer(construction)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ConstructionsDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            construction = ConstructionService.show(pk)
            serializer = ConstructionSerializer(construction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Construction.DoesNotExist:
            return Response(
                {"error": "Construction not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            serializer = ConstructionService.update(pk, request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Construction.DoesNotExist:
            return Response(
                {"error": "Construction not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            ConstructionService.destroy(pk)
            return Response(
                {"message": "Construction deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Construction.DoesNotExist:
            return Response(
                {"error": "Construction not found"}, status=status.HTTP_404_NOT_FOUND
            )


class ConstructionBasedStandardModelsAPIView(APIView):
    def post(self, request, pk):
        construction_project_name = request.data.get("project_name")
        location = request.data.get("location")
        description = request.data.get("description")

        if not construction_project_name or not location or not description:
            return Response(
                {"error": "Project name, location, and description are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        standard_model = get_object_or_404(StandardModel, id=pk)

        construction = Construction.objects.create(
            project_name=construction_project_name,
            location=location,
            description=description,
        )

        construction.referentials.set(standard_model.referentials.all())
        construction.observations.set(standard_model.observations.all())

        serializer = ConstructionSerializer(construction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
