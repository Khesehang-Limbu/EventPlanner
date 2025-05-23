# Generated by Django 5.2 on 2025-04-10 11:03

import apps.venue.constants
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='city/')),
            ],
        ),
        migrations.CreateModel(
            name='VenueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('capacity', models.PositiveIntegerField()),
                ('location_text', models.CharField(blank=True, max_length=300, null=True)),
                ('location_embed', models.TextField(blank=True, null=True)),
                ('available_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venue.city')),
            ],
        ),
        migrations.CreateModel(
            name='VenueImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='venue_images/')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.venuemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=apps.venue.constants.FoodType.choices, default=apps.venue.constants.FoodType['VEG'], max_length=20)),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venue.venuemodel')),
            ],
        ),
    ]
