# Generated by Django 3.1.7 on 2022-01-22 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Travels_Blogs', '0007_auto_20220122_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels_blogs',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
