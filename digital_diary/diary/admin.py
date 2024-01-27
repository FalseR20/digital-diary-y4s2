from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('course', 'subject', 'teacher', 'year')


@admin.register(models.Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'value', 'program', 'date')
