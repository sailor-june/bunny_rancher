# Generated by Django 4.1.5 on 2023-02-14 14:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0008_alter_bunny_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bunny",
            name="active",
        ),
    ]
