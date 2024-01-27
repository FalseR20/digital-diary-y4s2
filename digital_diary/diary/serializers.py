from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'user')

    user = UserSerializer()


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('id', 'user')

    user = UserSerializer()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'students')

    students = StudentSerializer(many=True, read_only=True)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        fields = ('id', 'course', "subject", "teacher", 'year')

    course = CourseSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = ('id', 'student', 'program', 'date', 'value', 'note')

    student = UserSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)
