# Generated by Django 4.0.1 on 2022-02-23 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_alter_project_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeentry',
            name='tags',
        ),
    ]
