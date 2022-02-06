# Generated by Django 4.0.1 on 2022-02-06 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_project_billable_project_billable_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayentry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayentry',
            name='time_total',
            field=models.IntegerField(default=0),
        ),
    ]
