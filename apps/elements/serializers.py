from rest_framework import serializers
from .models import Element, ElementType


class ElementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementType
        fields = ['id', 'name']


class ElementSerializer(serializers.ModelSerializer):
    element_type = ElementTypeSerializer(read_only=True)
    element_type_id = serializers.IntegerField(write_only=True)
    materials = serializers.StringRelatedField(many=True, read_only=True)
    material_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Element
        fields = ['id', 'element_type', 'element_type_id', 'materials', 'material_ids']

    def create(self, validated_data):
        material_ids = validated_data.pop('material_ids', [])
        element = Element.objects.create(**validated_data)
        if material_ids:
            element.materials.set(material_ids)
        return element

    def update(self, instance, validated_data):
        material_ids = validated_data.pop('material_ids', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if material_ids is not None:
            instance.materials.set(material_ids)
        
        return instance