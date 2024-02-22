# Generated by Django 5.0.1 on 2024-02-10 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_classschedule'),
        ('users', '0005_alter_imuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attended_classes', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_attendances', to='users.imuser')),
                ('class_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='main.classschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('resolution_status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('DECLINED', 'Declined'), ('RESOLVED', 'Resolved')], default='PENDING', max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_queries', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_queries', to='users.imuser')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_queries', to='users.imuser')),
            ],
        ),
        migrations.CreateModel(
            name='QueryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='written_comments', to='users.imuser')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.query')),
            ],
        ),
    ]
