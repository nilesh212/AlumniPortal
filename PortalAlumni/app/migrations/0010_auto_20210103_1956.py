# Generated by Django 3.1.4 on 2021-01-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_eventmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='event_pics/'),
        ),
    ]
