# Generated by Django 3.2.17 on 2023-11-10 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appteste', '0001_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unsplashimg_id',
            field=models.CharField(default='', max_length=150),
        ),
    ]
