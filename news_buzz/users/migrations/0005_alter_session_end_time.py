# Generated by Django 4.2.5 on 2023-10-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_participant_session"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="end_time",
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name="time session ended"),
        ),
    ]