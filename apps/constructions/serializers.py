from rest_framework import serializers
from .models import Construction
from apps.referentials.models import Referential
from apps.observations.serializers import ObservationSerializer


class ConstructionSerializer(serializers.ModelSerializer):
    referentials = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Referential.objects.all()
    )
    observations = ObservationSerializer(many=True, read_only=True)

    class Meta:
        model = Construction
        fields = [
            "id",
            "project_name",
            "location",
            "description",
            "aprovation_status",
            "creation_date",
            "aprovation_observations",
            "referentials",
            "observations",
            "is_active",
        ]

    def create(self, validated_data):
        referentials = validated_data.pop("referentials", [])
        observations = validated_data.pop("observations", [])

        construction = Construction.objects.create(**validated_data)

        # associa os m2m após a criação
        construction.referentials.set(referentials)
        construction.observations.set(observations)

        return construction

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
