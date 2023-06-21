import io

from rest_framework import serializers
from .models import HistoricalObject
from .models import ObjectTypes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class HistoricalObjectModel:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description


class HistoricalObjectSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=255)
    object_type = serializers.SlugRelatedField(slug_field='name', queryset=ObjectTypes.objects.all())
    description = serializers.CharField()

    def create(self, validated_data):
        return HistoricalObject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.object_type = validated_data.get('object_type', instance.object_type)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


# def encode():
#     model = HistoricalObject('Super pamyatnik', 'Opisanie super pamyatnika')
#     model_sr = HistoricalObjectSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"Super pamyatnik","description":"Opisanie super pamyatnika"}')
#     data = JSONParser().parse(stream)
#     print(data)
#     serializer = HistoricalObjectSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.data)


# class HistoricalObjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Monument
#         fields = ('name', 'object_type')
