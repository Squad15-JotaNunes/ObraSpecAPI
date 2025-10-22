from rest_framework import serializers
from .models import Referential, ReferentialName
from apps.areas.models import Area
from apps.areas.serializers import AreaSerializer


class ReferentialNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferentialName
        fields = ["id", "name"]


class ReferentialSerializer(serializers.ModelSerializer):
    referential_name = ReferentialNameSerializer(read_only=True)
    referential_name_id = serializers.PrimaryKeyRelatedField(
        queryset=ReferentialName.objects.all(),
        source="referential_name",
        write_only=True,
    )

    areas = AreaSerializer(many=True, read_only=True)
    areas_ids = serializers.PrimaryKeyRelatedField(
        queryset=Area.objects.all(), many=True, source="areas", write_only=True
    )

    class Meta:
        model = Referential
        fields = [
            "id",
            "referential_name",
            "referential_name_id",
            "areas",
            "areas_ids",
            "is_approved",
            "comment",
        ]
