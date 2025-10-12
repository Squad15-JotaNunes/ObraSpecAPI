from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.constructions.models import Construction
from apps.standard_models.models import StandardModel
from apps.standard_models.services import StandardModelService
from apps.standard_models.serializer import StandardModelSerializer


class StandardModelListAPIView(APIView):
    def get(self, request):
        try:
            standard_models = StandardModelService.index()
            serializer = StandardModelSerializer(standard_models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class StandardModelDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            standard_model = StandardModelService.show(pk)
            serializer = StandardModelSerializer(standard_model)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StandardModel.DoesNotExist:
            return Response(
                {"error": "Standard model not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            serializer = StandardModelService.update(pk, request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StandardModel.DoesNotExist:
            return Response(
                {"error": "Standard model not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            StandardModelService.destroy(pk)
            return Response(
                {"message": "Standard model deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except StandardModel.DoesNotExist:
            return Response(
                {"error": "Standard model not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, pk):
        try:
            standard_model_name = request.data.get("name")
            construction = Construction.objects.get(pk=pk)

            standard_model = StandardModel.objects.create(name=standard_model_name)

            standard_model.referentials.set(construction.referentials.all())
            standard_model.observations.set(construction.observations.all())

            serializer = StandardModelSerializer(standard_model)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Construction.DoesNotExist:
            return Response(
                {"error": "Construction model not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
