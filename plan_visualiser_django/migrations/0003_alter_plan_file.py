# Generated by Django 4.1.2 on 2022-10-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plan_visualiser_django", "0002_plan_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="file",
            field=models.FileField(null=True, upload_to="plan_files"),
        ),
    ]