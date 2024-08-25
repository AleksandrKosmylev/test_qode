# Generated by Django 4.2.10 on 2024-08-25 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_price'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
    ]
