# Generated by Django 5.1.4 on 2025-01-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_comment_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="time",
            field=models.TimeField(auto_now=True),
        ),
    ]
