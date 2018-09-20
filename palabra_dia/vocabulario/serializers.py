from rest_framework import serializers
from vocabulario.models import Vocabulario

class VocabularioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    palabra = serializers.CharField(required=False, allow_blank=True, max_length=100)
    definicion = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Vo` instance, given the validated data.
        """
        return Vocabulario.objects.create(**validated_data)
   