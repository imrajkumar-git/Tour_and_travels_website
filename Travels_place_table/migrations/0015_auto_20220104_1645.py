# Generated by Django 3.1.7 on 2022-01-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_place_table', '0014_auto_20220104_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelsplacesinformation',
            name='Difficulty_level',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='travelsplacesinformation',
            name='From',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='travelsplacesinformation',
            name='Max_Evaluation',
            field=models.IntegerField(default='2000'),
        ),
        migrations.AddField(
            model_name='travelsplacesinformation',
            name='To',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
