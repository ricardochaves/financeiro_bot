# Generated by Django 2.2.8 on 2020-06-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokes_note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='paper',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
