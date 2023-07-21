# Generated by Django 4.2.2 on 2023-07-20 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TBL_Usuario",
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
                ("payroll", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TBL_Video",
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
                ("name", models.CharField(max_length=50)),
                ("extension", models.CharField(max_length=5)),
                ("size", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TBL_Video_Usuario",
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
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_user_id",
                        to="videos.tbl_usuario",
                    ),
                ),
                (
                    "video_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_video_id",
                        to="videos.tbl_video",
                    ),
                ),
            ],
        ),
    ]