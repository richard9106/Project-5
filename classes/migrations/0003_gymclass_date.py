# Generated by Django 5.0.5 on 2024-07-19 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_rename_image_gymclass_image_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymclass',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]