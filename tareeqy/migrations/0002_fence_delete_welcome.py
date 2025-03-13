# Generated by Django 5.1.7 on 2025-03-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tareeqy", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="Welcome",
        ),
    ]
