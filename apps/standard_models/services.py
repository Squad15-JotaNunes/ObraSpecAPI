from apps.standard_models.models import StandardModel
from apps.standard_models.serializer import StandardModelSerializer


class StandardModelService:
    @staticmethod
    def store(data):
        return StandardModel.objects.create(**data)

    @staticmethod
    def show(pk):
        return StandardModel.objects.get(pk=pk)

    @staticmethod
    def index():
        return StandardModel.objects.all()

    @staticmethod
    def update(pk, validated_data):
        standard_model = StandardModel.objects.get(pk=pk)
        serializer = StandardModelSerializer(
            standard_model, data=validated_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer

    @staticmethod
    def destroy(pk):
        standard_model = StandardModel.objects.get(pk=pk)
        standard_model.delete()
        return True
