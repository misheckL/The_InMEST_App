# Generated by Django 5.0.1 on 2024-02-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_imuser_first_name_alter_imuser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imuser',
            name='USER_TYPE',
            field=models.CharField(choices=[('choice', 'SELECT USER'), ('EIT', 'EIT'), ('Teaching Fellow', 'TEACHING FELLOW'), ('Admin Staff', 'ADMIN STAFF'), ('Admin', 'ADMIN')], max_length=50),
        ),
    ]
