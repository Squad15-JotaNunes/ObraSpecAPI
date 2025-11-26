from rest_framework import serializers
from .models import Construction
from apps.referentials.models import Referential
from apps.observations.models import Observation
from apps.referentials.serializers import ReferentialSerializer
from apps.observations.serializers import ObservationSerializer


class ConstructionSerializer(serializers.ModelSerializer):
    referentials = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Referential.objects.all()
    )
    observations = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Observation.objects.all()
    )

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
        construction.referentials.set(referentials)
        construction.observations.set(observations)
        return construction

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["referentials"] = ReferentialSerializer(
            instance.referentials.all(), many=True
        ).data

        representation["observations"] = ObservationSerializer(
            instance.observations.all(), many=True
        ).data

        return representation