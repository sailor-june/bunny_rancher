# Generated by Django 4.1.5 on 2023-02-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0007_alter_bunny_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bunny",
            name="name",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]