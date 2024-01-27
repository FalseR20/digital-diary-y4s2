from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from digital_diary.diary.utils import get_current_year

User = get_user_model()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=8)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return f"Course {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"Subject {self.name}"


class Program(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField(unique=True, blank=True, default=get_current_year)

    def __str__(self):
        return f"{self.subject} for {self.course} by {self.teacher}"


class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=date.today)
    value = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} got {self.note} in {self.program} on {self.date}"
