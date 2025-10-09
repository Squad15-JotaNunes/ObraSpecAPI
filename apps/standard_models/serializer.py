from rest_framework import serializers
from .models import StandardModel
from apps.referentials.models import Referential
from apps.observations.models import Observation


class StandardModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    referentials = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Referential.objects.all()
    )
    observations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Observation.objects.all()
    )

    class Meta:
        model = StandardModel
        fields = [
            "id",
            "name",
            "num_housing_units",
            "num_adapted_units",
            "land_area",
            "referentials",
            "observations",
        ]

    def validate_name(self, value):
        if len(value.strip()) <= 0:
            raise serializers.ValidationError("The field name must not be empty")
        return value
