# Generated by Django 4.1.2 on 2023-01-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plan_visualiser_django", "0018_planfield_required_flag"),
    ]

    operations = [
        migrations.AddField(
            model_name="planfield",
            name="sort_index",
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
