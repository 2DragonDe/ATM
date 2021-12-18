# Generated by Django 3.1.4 on 2021-02-18 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_report24h'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandlingStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handling_staff', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='end_funds',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='replace_components',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='to_funds',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='handling_staff_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.handlingstaff'),
        ),
    ]
