# Generated by Django 5.0.7 on 2024-09-30 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0031_restaurant_businesspermit'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
