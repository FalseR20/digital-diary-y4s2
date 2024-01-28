from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from digital_diary.diary.utils import get_current_year

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"course {self.name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"student {self.user}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"teacher {self.user}"


class Subject(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"subject {self.name}"


class Program(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"program {self.subject} for {self.course} by {self.teacher}"


class Lesson(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=date.today)
    homework = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"lesson of {self.program} on {self.date}"


class Mark(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    note = models.TextField(blank=True)

    def __str__(self):
        return f"mark {self.note} of {self.student} at {self.lesson}"
