# Generated by Django 4.0.1 on 2022-02-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_remove_project_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
