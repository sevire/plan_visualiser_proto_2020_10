# Generated by Django 4.1.5 on 2023-01-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plan_visualiser_django", "0020_remove_planmappedfield_plan_field_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="plan",
            constraint=models.UniqueConstraint(
                fields=("user", "original_file_name"), name="unique_filename_for_user"
            ),
        ),
    ]