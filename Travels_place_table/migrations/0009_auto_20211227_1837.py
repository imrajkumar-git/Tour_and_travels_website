# Generated by Django 3.1.7 on 2021-12-27 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_place_table', '0008_auto_20211227_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travels_place_table.travelsplacepath'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='Start_and_end_Path',
            field=models.CharField(db_index=True, default='pokhara', max_length=400, null=True),
        ),
    ]
