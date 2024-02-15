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


class HistoricalObjectSerializer(serializers.ModelSerializer):
    object_type = serializers.CharField(source="object_type.name")

    class Meta:
        model = HistoricalObject
        fields = ("name", "object_type", "description")

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
