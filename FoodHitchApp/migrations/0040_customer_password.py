# Generated by Django 5.0.7 on 2024-10-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0039_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Password',
            field=models.CharField(default='', max_length=128),
        ),
    ]
