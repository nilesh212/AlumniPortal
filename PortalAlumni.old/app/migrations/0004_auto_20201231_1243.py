# Generated by Django 3.1.4 on 2020-12-31 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20201231_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='post',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
