# Generated by Django 3.1.7 on 2021-12-28 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_place_table', '0009_auto_20211227_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelsplacesinformation',
            name='Travels_package_type',
        ),
    ]
