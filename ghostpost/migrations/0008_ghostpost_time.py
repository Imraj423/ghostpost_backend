# Generated by Django 3.0.3 on 2020-02-10 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0007_remove_ghostpost_submitdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghostpost',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
