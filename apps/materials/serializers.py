from rest_framework import serializers
from apps.materials.models import Brand, Material, MaterialType


class BrandSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if len(value.strip()) == 0 or len(value) > 50:
            raise serializers.ValidationError(
                "The field name must be between 1 and 50 chars"
            )
        return value

    class Meta:
        model = Brand
        fields = ["id", "name"]


class MaterialTypeSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if len(value) <= 0 or len(value) > 50:
            raise serializers.ValidationError(
                "The field name must be between 1 and 50 chars"
            )
        return value

    class Meta:
        model = MaterialType
        fields = ["id", "name"]


class MaterialSerializer(serializers.ModelSerializer):

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
