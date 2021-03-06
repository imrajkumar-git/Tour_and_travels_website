# Generated by Django 3.1.7 on 2021-12-26 11:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Travels_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, default='regular', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='travels_package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Travels_package_name', models.CharField(db_index=True, max_length=250)),
                ('Travels_package_category', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Travelsplacesinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_cost', models.IntegerField(default='1000', validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1000)])),
                ('discount', models.IntegerField(default='10%', validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(0)])),
                ('travel_place_title', models.CharField(default='Dhading Simle Trek', max_length=250)),
                ('Tour_operator', models.CharField(default='stravels', max_length=25)),
                ('max_group_size', models.IntegerField(default='10')),
                ('Max_range', models.IntegerField(default='2')),
                ('Min_range', models.IntegerField(default='20')),
                ('operate_language', models.CharField(default='english', max_length=20)),
                ('Travels_place_Description', models.TextField()),
                ('travels_place_image', models.ImageField(blank=True, null=True, upload_to='places/%Y/%m/')),
                ('travels_place_image1', models.ImageField(blank=True, null=True, upload_to='places/%Y/%m/')),
                ('travels_place_image2', models.ImageField(blank=True, null=True, upload_to='places/%Y/%m/')),
                ('duration', models.CharField(blank=True, max_length=20, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True)),
                ('slug', models.SlugField(max_length=200)),
                ('map', models.CharField(max_length=80, null=True)),
                ('Travels_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travels_place_table.travels_category')),
                ('Travels_package_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travels_place_table.travels_package')),
            ],
        ),
        migrations.CreateModel(
            name='User_rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)])),
                ('travels_place_information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to='Travels_place_table.travelsplacesinformation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TravelsPlacePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(db_index=True, default='pokhara', max_length=200)),
                ('route_information', models.TextField()),
                ('route_picture', models.ImageField(blank=True, null=True, upload_to='places/')),
                ('travels_place_information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Travels_place_path', to='Travels_place_table.travelsplacesinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Travels_Package_Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checking_date', models.DateField(blank=True, default='2021-12-23')),
                ('is_booked', models.BooleanField(default='True')),
                ('check_out_date', models.DateField(blank=True, default='2021-12-27')),
                ('No_of_people', models.IntegerField(default='4', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('User', models.ForeignKey(default='41', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('destination_name', models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='Travels_place_table.travelsplacesinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.DateField(null=True)),
                ('TO', models.DateField(null=True)),
                ('month_name', models.CharField(max_length=50)),
                ('travels_place_information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departure_Date', to='Travels_place_table.travelsplacesinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'available'), ('2', 'not available')], default='aviable', max_length=50)),
                ('day_name', models.CharField(max_length=100)),
                ('num_stars', models.IntegerField()),
                ('Month', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suitable_days', to='Travels_place_table.month')),
            ],
        ),
    ]
