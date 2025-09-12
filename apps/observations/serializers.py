from rest_framework import serializers

from .models import Observation


class ObservationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Observation
        fields = ["id", "description"]

    def validate_description(self, value):
        if len(value.strip()) <= 0:
            raise serializers.ValidationError(
                "The field description must be greater than 0 chars"
            )
        return value
