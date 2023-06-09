# Generated by Django 4.2.1 on 2023-05-08 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("submissions", "0003_alter_hackathon_start_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="HackathonRegistration",
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
                ("registered_at", models.DateTimeField(auto_now_add=True)),
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
            options={
                "unique_together": {("hackathon", "user")},
            },
        ),
    ]
