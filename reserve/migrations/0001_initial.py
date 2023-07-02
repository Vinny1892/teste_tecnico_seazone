# Generated by Django 4.2.2 on 2023-07-02 20:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("announcement", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reserve",
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
                ("code", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("quantity_guests", models.IntegerField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("comment", models.CharField(max_length=256)),
                ("check_in", models.DateTimeField()),
                ("check_out", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "announcement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="announcement.announcement",
                    ),
                ),
            ],
        ),
    ]