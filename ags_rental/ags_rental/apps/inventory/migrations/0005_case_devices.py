# Generated by Django 4.2 on 2023-05-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_alter_case_contains"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="devices",
            field=models.ManyToManyField(to="inventory.device"),
        ),
    ]
