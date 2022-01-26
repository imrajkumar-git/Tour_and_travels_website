# Generated by Django 3.1.7 on 2022-01-25 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_place_table', '0042_auto_20220122_1344'),
        ('Travels_Blogs', '0009_auto_20220122_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='Our own title', max_length=35)),
                ('Activity_Level', models.CharField(default='Modarate', max_length=1000)),
                ('Age', models.IntegerField(default='14+')),
                ('Duration', models.CharField(default='14D', max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travels_place_table.travels_category')),
            ],
        ),
    ]
