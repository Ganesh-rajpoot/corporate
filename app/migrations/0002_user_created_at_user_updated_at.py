# Generated by Django 5.0.4 on 2024-04-13 23:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]