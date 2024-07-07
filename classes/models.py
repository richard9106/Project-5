"""manage gym classes """
from django.db import models
from users.models import CustomUser
from datetime import time

class GymClass(models.Model):
    """ list of classes"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ], default="Monday")
    time = models.TimeField(default=time(9, 0))
    image = models.ImageField(upload_to='static/class_images/', default="images/default_class.jpg")

    def __str__(self):
        return self.name

class Booking(models.Model):
    """manage booking classes"""
    user_booking = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_booking} - {self.gym_class.name}'