# Generated by Django 3.1.4 on 2021-02-15 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='event',
            new_name='event_comment',
        ),
    ]
