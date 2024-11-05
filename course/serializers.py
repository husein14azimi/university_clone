from rest_framework import serializers
from django.db import IntegrityError
from .models import Course, CourseStep, Student, CourseStudentRelationship


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseStepSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = CourseStep
        fields = '__all__'


class StudentCoursesSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = CourseStudentRelationship
        fields = ['course_name',]


class StudentSerializer(serializers.ModelSerializer):
    courses = StudentCoursesSerializer(source='coursestudentrelationship_set', many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class CourseStudentRelationshipSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    student_full_name = serializers.CharField(source='student.full_name', read_only=True)

    class Meta:
        model = CourseStudentRelationship
        fields = '__all__'