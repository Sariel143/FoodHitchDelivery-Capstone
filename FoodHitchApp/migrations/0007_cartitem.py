# Generated by Django 5.0.7 on 2024-09-11 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0006_menu_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodName', models.CharField(max_length=255)),
                ('Quantity', models.IntegerField(default=1)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodHitchApp.customer')),
                ('FoodID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodHitchApp.menu')),
            ],
        ),
    ]
