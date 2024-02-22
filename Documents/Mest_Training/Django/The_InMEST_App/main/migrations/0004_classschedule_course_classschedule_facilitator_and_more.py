# Generated by Django 5.0.1 on 2024-02-22 10:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_query_resolution_status_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="classschedule",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="course_class_schedule",
                to="main.course",
            ),
        ),
        migrations.AddField(
            model_name="classschedule",
            name="facilitator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="facilitator_class_schedule",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="classschedule",
            name="meeting_types",
            field=models.CharField(
                choices=[
                    ("CLASS_SECTIONS", "Class Sessions"),
                    ("WELLNESS_SESSIONS", "Well Session"),
                    ("GUEST_LECTURE", "Guest Lecture"),
                ],
                default="CLASS SESSIONS",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="classschedule",
            name="repeat_frequency",
            field=models.CharField(
                choices=[
                    ("DAILY", "Daily"),
                    ("WEEKLY", "Weekly"),
                    ("MONTHLY", "Monthly"),
                ],
                default="DAILY",
                max_length=20,
            ),
        ),
    ]
