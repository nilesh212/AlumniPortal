# Generated by Django 3.1.4 on 2021-01-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_eventmodel_number_of_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='number_of_comments',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
