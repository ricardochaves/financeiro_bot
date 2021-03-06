# Generated by Django 2.2.7 on 2019-11-28 00:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("nubank", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="NubankCards",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("command_1", models.CharField(max_length=11)),
                ("command_2", models.CharField(max_length=11)),
                ("cpf", models.CharField(max_length=11)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="NubankSession",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("session_id", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="NubankStatement",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=9)),
                ("amount_without_iof", models.DecimalField(decimal_places=2, max_digits=9)),
                ("description", models.CharField(blank=True, max_length=200, null=True)),
                ("category", models.CharField(blank=True, max_length=80, null=True)),
                ("source", models.CharField(blank=True, max_length=40, null=True)),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                ("account", models.CharField(blank=True, max_length=40, null=True)),
                ("details", django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ("nubank_id", models.CharField(blank=True, db_index=True, max_length=40, null=True, verbose_name="id")),
                ("href", models.CharField(blank=True, max_length=200, null=True)),
                ("item_time", models.DateTimeField()),
                ("is_processed", models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(name="NubankItem"),
        migrations.DeleteModel(name="NubankItem2"),
    ]
