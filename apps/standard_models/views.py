from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.constructions.models import Construction
from .serializers import StandardModelSerializer
from .services.standard_model_service import StandardModelService
from .models import StandardModel


class StandardModelListAPIView(APIView):
    def get(self, request):
        try:
            standard_models = StandardModelService.index()
            serializer = StandardModelSerializer(standard_models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            data = request.data.copy()
            construction_id = data.get("construction_id")

            if construction_id:
                try:
                    construction = Construction.objects.get(id=construction_id)
                except Construction.DoesNotExist:
                    return Response(
                        {"error": "Construction not found"},
                        status=status.HTTP_404_NOT_FOUND
                    )

                data.setdefault("num_housing_units", construction.num_housing_units)
                data.setdefault("num_adapted_units", construction.num_adapted_units)
                data.setdefault("land_area", construction.land_area)
                data.setdefault("referentials", [r.id for r in construction.referentials.all()])
                data.setdefault("observations", [o.id for o in construction.observations.all()])

            serializer = StandardModelSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            standard_model = StandardModelService.store(serializer.validated_data)
            output = StandardModelSerializer(standard_model)

            return Response(output.data, status=status.HTTP_201_CREATED)

        except Exception as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class StandardModelDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            standard_model = StandardModelService.show(pk)
            serializer = StandardModelSerializer(standard_model)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StandardModel.DoesNotExist:
            return Response(
                {"error": "Standard model not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, pk):
        try:
            serializer = StandardModelService.update(pk, request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StandardModel.DoesNotExist:
            return Response(
                {"error": "Standard model not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        try:
            StandardModelService.destroy(pk)
            return Response(
                {"message": "Standard model deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except StandardModel.DoesNotExist:
            return Response(
                {"error": "Standard model not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
