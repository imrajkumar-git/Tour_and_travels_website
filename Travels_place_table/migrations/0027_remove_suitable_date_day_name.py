# Generated by Django 3.1.7 on 2022-01-07 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_place_table', '0026_auto_20220106_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suitable_date',
            name='day_name',
        ),
    ]