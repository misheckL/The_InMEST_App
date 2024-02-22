# Generated by Django 5.0.1 on 2024-02-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imuser',
            name='FIRST_NAME',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='imuser',
            name='LAST_NAME',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='imuser',
            name='USER_TYPE',
            field=models.CharField(choices=[('EIT', 'EIT'), ('Teaching Fellow', 'TEACHING FELLOW'), ('Admin Staff', 'ADMIN STAFF'), ('Admin', 'ADMIN')], max_length=50),
        ),
    ]