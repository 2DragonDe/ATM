# Generated by Django 3.1.4 on 2021-02-01 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210201_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='error',
            name='status',
        ),
    ]