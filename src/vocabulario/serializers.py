from rest_framework import serializers
from vocabulario.models import Vocabulario

class VocabularioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    palabra = serializers.CharField(required=False, allow_blank=True, max_length=100)
    definicion = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Vocabulario` instance, given the validated data.
        """
        return Vocabulario.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.palabra = validated_data.get('word', instance.word)
        instance.definicion = validated_data.get('definition', instance.definition)
        return instance

    

   