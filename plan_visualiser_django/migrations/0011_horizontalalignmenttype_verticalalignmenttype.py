# Generated by Django 4.1.2 on 2023-01-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plan_visualiser_django", "0010_plotableshape_plotableshapetype_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HorizontalAlignmentType",
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
                    "horizontal_alignment_name",
                    models.CharField(
                        choices=[("LFT", "Left"), ("CNT", "Center"), ("RGT", "Right")],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VerticalAlignmentType",
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
                    "vertical_alignment_name",
                    models.CharField(
                        choices=[("TOP", "Top"), ("MID", "Middle"), ("BTM", "Bottom")],
                        max_length=3,
                    ),
                ),
            ],
        ),
    ]