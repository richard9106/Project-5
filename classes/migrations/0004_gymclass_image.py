# Generated by Django 5.0.5 on 2024-07-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_remove_gymclass_schedule_gymclass_day_of_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymclass',
            name='image',
            field=models.ImageField(default='default_class.jpg', upload_to='static/class_images/'),
        ),
    ]