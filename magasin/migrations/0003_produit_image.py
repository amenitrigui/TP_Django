# Generated by Django 5.0.1 on 2024-02-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_alter_produit_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='media/'),
        ),
    ]
