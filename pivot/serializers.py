from rest_framework import serializers

from .models import Zoo, Animal, AnimalCount


class ZooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zoo
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalCount
        fields = '__all__'