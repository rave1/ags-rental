# Generated by Django 4.2 on 2023-05-11 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0005_case_devices"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="case",
            name="contains",
        ),
    ]
