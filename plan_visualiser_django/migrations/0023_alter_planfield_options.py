# Generated by Django 4.1.5 on 2023-01-29 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("plan_visualiser_django", "0022_filetype_plan_field_mapping_type_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="planfield", options={"ordering": ("sort_index",)},
        ),
    ]
