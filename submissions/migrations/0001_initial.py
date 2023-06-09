# Generated by Django 4.2.1 on 2023-05-06 20:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hackathon",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("background_image", models.ImageField(upload_to="images/")),
                ("hackathon_image", models.ImageField(upload_to="images/")),
                (
                    "submission_type",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("file", "File"),
                            ("link", "Link"),
                        ],
                        max_length=20,
                    ),
                ),
                ("start_date", models.DateTimeField(default=datetime.datetime.now)),
                ("end_date", models.DateTimeField()),
                ("reward_prize", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Submission",
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
                ("name", models.CharField(max_length=200)),
                ("summary", models.TextField()),
                (
                    "submission_file",
                    models.FileField(blank=True, null=True, upload_to="submissions/"),
                ),
                (
                    "submission_image",
                    models.ImageField(blank=True, null=True, upload_to="submissions/"),
                ),
                ("submission_link", models.URLField(blank=True, null=True)),
                (
                    "hackathon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="submissions.hackathon",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
