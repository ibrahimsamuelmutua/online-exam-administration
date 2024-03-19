# Generated by Django 3.0.5 on 2024-03-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='status',
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mobile',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pic/Teacher/'),
        ),
    ]
