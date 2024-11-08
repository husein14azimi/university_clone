# Generated by Django 5.1.2 on 2024-11-02 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_coursestudentrelationship_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestudentrelationship',
            name='semester',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_four_digit_number', message='Enter a 4-digit number between 1000 and 9999', regex='^[1-9]\\d{3}$')]),
        ),
    ]
