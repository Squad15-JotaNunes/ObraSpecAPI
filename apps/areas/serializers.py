from rest_framework import serializers
from apps.areas.models import Area, AreaName
from apps.elements.serializers import ElementSerializer
from apps.elements.models import Element


class AreaNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaName
        fields = ["id", "name"]


class AreaSerializer(serializers.ModelSerializer):
    area_name = AreaNameSerializer(read_only=True)
    area_name_id = serializers.PrimaryKeyRelatedField(
        queryset=AreaName.objects.all(), source="area_name", write_only=True
    )
    elements = ElementSerializer(many=True, read_only=True)
    elements_ids = serializers.PrimaryKeyRelatedField(
        queryset=Element.objects.all(), many=True, source="elements", write_only=True
    )

    class Meta:
        model = Area
        fields = ["id", "area_name", "area_name_id", "elements", "elements_ids"]
