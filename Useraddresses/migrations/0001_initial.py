# Generated by Django 3.1.7 on 2021-12-21 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressLine1', models.CharField(default='your street/tole name', max_length=250)),
                ('addressLine2', models.CharField(blank=True, max_length=250, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(default='Nepal', max_length=100)),
                ('phone_number', models.CharField(default='phonenumbers', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
