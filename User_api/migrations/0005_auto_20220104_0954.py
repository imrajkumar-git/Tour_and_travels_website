# Generated by Django 3.1.7 on 2022-01-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_api', '0004_auto_20220103_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Profile_Image',
            field=models.ImageField(default='/profile_icon/1.jpg', upload_to='user/%Y/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
