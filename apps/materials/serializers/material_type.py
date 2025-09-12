from rest_framework import serializers

from apps.materials.models import MaterialType


class MaterialTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialType
        fields = ["id", "name"]

    id = serializers.IntegerField(read_only=True)

    def validate_name(self, value):
        if len(value) <= 0 or len(value) > 50:
            raise serializers.ValidationError(
                "The field name must be between 1 and 50 chars"
            )
        return value
