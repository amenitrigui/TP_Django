# Generated by Django 5.0.1 on 2024-04-28 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_produitc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='dateCde',
            field=models.DateField(default=datetime.date(2024, 4, 28), null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.FloatField(editable=False),
        ),
    ]
