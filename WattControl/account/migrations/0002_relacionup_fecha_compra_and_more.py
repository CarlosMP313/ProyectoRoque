# Generated by Django 4.2 on 2024-04-26 01:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relacionup',
            name='fecha_compra',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='relacionup',
            name='tiempo_garantia_anios',
            field=models.IntegerField(default=0),
        ),
    ]
