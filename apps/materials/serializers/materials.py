from rest_framework import serializers

from ..models import Material, MaterialType, Brand


class MaterialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = [
            "id",
            "description",
            "brand",
            "brand_name",
            "material_type",
            "material_type_name",
        ]

    id = serializers.IntegerField(read_only=True)
    brand_name = serializers.CharField(source="brand.name", read_only=True)
    material_type_name = serializers.CharField(
        source="material_type.name", read_only=True
    )

    def validate(self, attrs):
        brand = attrs.get("brand")
        material_type = attrs.get("material_type")

        if brand and material_type:
            if Material.objects.filter(
                brand=brand, material_type=material_type
            ).exists():
                raise serializers.ValidationError(
                    "The brand and material type combination must be unique"
                )
        return attrs

    def validate_description(self, value):
        if len(value) <= 0:
            raise serializers.ValidationError(
                "The description must be greater than 0 chars"
            )
        return value
