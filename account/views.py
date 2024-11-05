from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class PersonViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer