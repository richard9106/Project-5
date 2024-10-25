"""manage gym classes """
from datetime import time, date, datetime
from django.db import models
from profiles.models import Profile
from cloudinary.models import CloudinaryField


class GymClass(models.Model):
    """ list of classes"""
    current_date = datetime.now().date()
    name = models.CharField(max_length=100)
    description = models.TextField()
    day_of_week = models.CharField(max_length=10, default="Monday")
    time = models.TimeField(default=time(9, 0))
    date = models.DateField(default=date.today)
    image_class = CloudinaryField('image_class',
                                  default="images/default_class.jpg")

    def __str__(self):
        return self.name


class Booking(models.Model):
    """manage booking classes"""
    user_booking = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_booking} - {self.gym_class.name}'
