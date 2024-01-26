from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from digital_diary.diary.utils import get_current_year

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=8)
    year = models.IntegerField(unique=True, blank=True, default=get_current_year)
    students = models.ManyToManyField(User, related_name='classes')

    class Meta:
        unique_together = [['name', 'year']]

    def __str__(self):
        return f"Course {self.name} of {self.year}"


class Subject(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"Subject {self.name}"


class Program(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} for {self.course} by {self.teacher}"


class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=date.today)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} got {self.note} in {self.program} on {self.date}"
