from django.shortcuts import render

from rest_framework import viewsets
from django_pivot.pivot import pivot

from .models import Zoo, Animal, AnimalCount
from .serializers import ZooSerializer, AnimalSerializer, AnimalCountSerializer


class ZooViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ZooSerializer
    queryset = Zoo.objects.all()

class AnimalViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

class AnimalCountViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AnimalCountSerializer
    queryset = pivot(AnimalCount.objects.all(), 'animal', 'zoo', 'count')
    print(queryset)