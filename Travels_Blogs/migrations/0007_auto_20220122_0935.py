# Generated by Django 3.1.7 on 2022-01-22 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_Blogs', '0006_travels_blogs_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travels_Blogs_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blogs_Category', models.CharField(default='category', max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='travels_blogs',
            name='Blog_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Travels_Blogs.travels_blogs_category'),
        ),
    ]
