# Generated by Django 3.1.7 on 2022-01-22 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_place_table', '0039_auto_20220122_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelsplacesinformation',
            name='summary',
            field=models.CharField(default='your own world', max_length=2000),
        ),
    ]
