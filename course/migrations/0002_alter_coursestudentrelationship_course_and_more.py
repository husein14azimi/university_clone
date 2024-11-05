# Generated by Django 5.1.2 on 2024-11-02 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestudentrelationship',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.course'),
        ),
        migrations.AlterField(
            model_name='coursestudentrelationship',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.student'),
        ),
    ]