# Generated by Django 3.1.4 on 2021-01-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210110_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='number_of_comments',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
