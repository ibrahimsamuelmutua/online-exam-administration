# Generated by Django 3.0.5 on 2024-03-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20240313_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='exam_duration',
            field=models.PositiveIntegerField(default=60),
        ),
    ]
