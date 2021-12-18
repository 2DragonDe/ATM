# Generated by Django 3.1.4 on 2021-01-31 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_close',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_post',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
