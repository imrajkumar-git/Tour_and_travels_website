# Generated by Django 3.1.7 on 2021-12-26 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_place_table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travels_package_booking',
            name='No_of_people',
            field=models.IntegerField(default='3', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
