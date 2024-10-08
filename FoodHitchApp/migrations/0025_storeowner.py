# Generated by Django 5.0.7 on 2024-09-22 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0024_delete_partnerrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreOwner',
            fields=[
                ('OwnerID', models.BigAutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone', models.CharField(max_length=15, unique=True)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='owner_pictures')),
                ('Password', models.CharField(default='', max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Store Owners',
            },
        ),
    ]
