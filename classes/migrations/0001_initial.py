# Generated by Django 5.0.5 on 2024-07-18 09:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=10)),
                ('time', models.TimeField(default=datetime.time(9, 0))),
                ('image', models.ImageField(default='images/default_class.jpg', upload_to='static/class_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('user_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('gym_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.gymclass')),
            ],
        ),
    ]
