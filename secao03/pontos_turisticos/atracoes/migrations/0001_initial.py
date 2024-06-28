# Generated by Django 5.0.6 on 2024-06-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Atracao",
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
                ("nome", models.CharField(max_length=150)),
                ("descricao", models.TextField()),
                ("horario_func", models.TextField()),
                ("idade_minima", models.IntegerField()),
            ],
        ),
    ]
