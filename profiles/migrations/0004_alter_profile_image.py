# Generated by Django 5.0.5 on 2024-10-25 08:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_birthday_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='static/images/profile_images/default_profile.png', max_length=255, null=True),
        ),
    ]
