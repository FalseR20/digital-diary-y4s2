from rest_framework import serializers

from digital_diary.users.serializers import UserSerializer
from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('user', 'user_username', 'course', 'course_id')

    user = UserSerializer(read_only=True)
    user_username = serializers.CharField(write_only=True)
    course = CourseSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('user', 'user_username')

    user = UserSerializer(read_only=True)
    user_username = serializers.CharField(write_only=True)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        fields = (
            'id', 'course', 'course_id', "subject", "subject_id", "teacher", "teacher_username"
        )

    course = CourseSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True)
    subject = SubjectSerializer(read_only=True)
    subject_id = serializers.IntegerField(write_only=True)
    teacher = TeacherSerializer(read_only=True)
    teacher_username = serializers.CharField(write_only=True)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('id', 'program', 'program_id', 'date', 'homework')

    program = ProgramSerializer(read_only=True)
    program_id = serializers.IntegerField(write_only=True)


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = ('id', 'lesson', 'lesson_id', 'student', 'student_username', 'value', 'note')

    lesson = LessonSerializer(read_only=True)
    lesson_id = serializers.IntegerField(write_only=True)
    student = StudentSerializer(read_only=True)
    student_username = serializers.CharField(write_only=True)
