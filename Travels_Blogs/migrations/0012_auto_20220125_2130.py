# Generated by Django 3.1.7 on 2022-01-25 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Travels_Blogs', '0011_auto_20220125_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='Title',
            field=models.CharField(default='Our own title', max_length=3500),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='Our own title', max_length=3500)),
                ('summary', models.CharField(default='Our own title', max_length=7500)),
                ('content', models.TextField(default='write your own content')),
                ('Image', models.ImageField(blank=True, default='/profile_icon/1.jpg', upload_to='Article/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travels_Blogs.travels_blogs_category')),
            ],
        ),
    ]
