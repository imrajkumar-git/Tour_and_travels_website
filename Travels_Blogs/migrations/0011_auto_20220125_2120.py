# Generated by Django 3.1.7 on 2022-01-25 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_Blogs', '0010_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travels_Blogs.travels_blogs_category'),
        ),
    ]
