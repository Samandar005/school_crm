# Generated by Django 5.1.4 on 2024-12-29 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_deleted',
        ),
    ]
