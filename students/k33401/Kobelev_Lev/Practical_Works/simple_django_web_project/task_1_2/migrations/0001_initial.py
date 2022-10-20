# Generated by Django 4.1.2 on 2022-10-20 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("state_number", models.CharField(max_length=15)),
                ("brand", models.CharField(max_length=20)),
                ("model", models.CharField(max_length=20)),
                ("color", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
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
                ("first_name", models.CharField(max_length=30)),
                ("second_name", models.CharField(max_length=30)),
                ("birthday", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ownership",
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
                ("date_start", models.DateField()),
                ("date_end", models.DateField(null=True)),
                (
                    "ownership_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task_1_2.car"
                    ),
                ),
                (
                    "ownership_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task_1_2.owner"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DriverLicense",
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
                ("license_number", models.CharField(max_length=10)),
                ("type", models.CharField(max_length=10)),
                ("issue_date", models.DateField()),
                (
                    "license_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task_1_2.owner"
                    ),
                ),
            ],
        ),
    ]
