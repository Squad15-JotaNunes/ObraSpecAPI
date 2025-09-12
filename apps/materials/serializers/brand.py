from rest_framework import serializers

from apps.materials.models import Brand


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ["id", "name"]

    id = serializers.IntegerField(read_only=True)

    def validate_name(self, value):
        if len(value.strip()) == 0 or len(value) > 50:
            raise serializers.ValidationError(
                "The field name must be between 1 and 50 chars"
            )
        return value
