# Generated by Django 5.0.7 on 2024-09-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0032_restaurant_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
