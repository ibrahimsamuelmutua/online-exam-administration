# Generated by Django 3.0.5 on 2024-03-17 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20240317_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='exam_duration',
        ),
    ]
