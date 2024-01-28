# Generated by Django 4.2.5 on 2024-01-27 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("diary", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="program",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="diary.course"
            ),
        ),
        migrations.AddField(
            model_name="program",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="diary.subject"
            ),
        ),
        migrations.AddField(
            model_name="program",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="diary.teacher"
            ),
        ),
        migrations.AddField(
            model_name="mark",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="diary.program"
            ),
        ),
        migrations.AddField(
            model_name="mark",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(related_name="courses", to="diary.student"),
        ),
    ]