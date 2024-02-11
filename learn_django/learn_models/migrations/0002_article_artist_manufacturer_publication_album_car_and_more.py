# Generated by Django 5.0.2 on 2024-02-11 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learn_models", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("headline", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "article",
                "ordering": ["headline"],
            },
        ),
        migrations.CreateModel(
            name="Artist",
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
                ("name", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "artist",
            },
        ),
        migrations.CreateModel(
            name="Manufacturer",
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
                ("name", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "manufacturer",
            },
        ),
        migrations.CreateModel(
            name="Publication",
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
                ("title", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "publication",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Album",
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
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learn_models.artist",
                    ),
                ),
            ],
            options={
                "db_table": "album",
            },
        ),
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
                ("name", models.CharField(max_length=30)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="learn_models.manufacturer",
                    ),
                ),
            ],
            options={
                "db_table": "car",
            },
        ),
        migrations.CreateModel(
            name="Membership",
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
                ("date_pub", models.DateField()),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learn_models.article",
                    ),
                ),
                (
                    "publication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learn_models.publication",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="publications",
            field=models.ManyToManyField(
                through="learn_models.Membership", to="learn_models.publication"
            ),
        ),
        migrations.CreateModel(
            name="Song",
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
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="learn_models.album",
                    ),
                ),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learn_models.artist",
                    ),
                ),
            ],
            options={
                "db_table": "song",
            },
        ),
    ]