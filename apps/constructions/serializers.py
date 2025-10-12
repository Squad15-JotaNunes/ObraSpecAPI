from rest_framework import serializers
from .models import Construction
from apps.referentials.models import Referential
from apps.observations.models import Observation


class ConstructionSerializer(serializers.ModelSerializer):
    referentials = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Referential.objects.all()
    )
    observations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Observation.objects.all()
    )

    class Meta:
        model = Construction
        fields = [
            "id",
            "project_name",
            "location",
            "description",
            # "num_housing_units",
            # "num_adapted_units",
            # "land_area",
            "referentials",
            "observations",
            "is_active",
        ]

    def validate_project_name(self, value):
        if len(value.strip()) <= 0:
            raise serializers.ValidationError(
                "The field project_name must not be empty"
            )
        return value

    def validate_description(self, value):
        if len(value.strip()) <= 0:
            raise serializers.ValidationError("The field description must not be empty")
        return value
