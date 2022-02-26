# Generated by Django 3.1.7 on 2022-01-26 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Travels_place_table', '0042_auto_20220122_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departure_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('To', models.DateField(blank=True, null=True)),
                ('From', models.DateField(blank=True, null=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travels_place_table.travelsplacesinformation')),
                ('month_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travels_place_table.departure_month')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.DateField(blank=True, null=True)),
                ('To', models.DateField(blank=True, null=True)),
                ('No_of_people', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Package_Booking_app.departure_date')),
            ],
        ),
    ]