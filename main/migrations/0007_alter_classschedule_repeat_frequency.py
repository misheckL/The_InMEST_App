# Generated by Django 5.0.1 on 2024-02-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_classattendance_query_querycomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='repeat_frequency',
            field=models.CharField(blank=True, choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly')], max_length=25, null=True),
        ),
    ]