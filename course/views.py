from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers

# Create your views here.
class CourseList(ListCreateAPIView):
    def get_queryset(self):
        return models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
class CourseDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    

class CourseStepList(ListCreateAPIView):
    def get_queryset(self):
        return models.CourseStep.objects.all()
    serializer_class = serializers.CourseStepSerializer
class CourseStepDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return models.CourseStep.objects.all()
    serializer_class = serializers.CourseStepSerializer

    

class StudentList(ListCreateAPIView):
    def get_queryset(self):
        return models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
class StudentDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    

class CourseStudentRelationshipList(ListCreateAPIView):
    def get_queryset(self):
        return models.CourseStudentRelationship.objects.all()
    serializer_class = serializers.CourseStudentRelationshipSerializer
class CourseStudentRelationshipDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return models.CourseStudentRelationship.objects.all()
    serializer_class = serializers.CourseStudentRelationshipSerializer
    

    