# Generated by Django 3.1.7 on 2022-01-05 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_api', '0005_auto_20220104_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='kathmandu', max_length=30),
        ),
    ]
