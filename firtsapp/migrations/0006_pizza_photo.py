# Generated by Django 3.0.5 on 2020-04-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firtsapp', '0005_auto_20200413_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='firtsapp/photos', verbose_name='Фото'),
        ),
    ]
