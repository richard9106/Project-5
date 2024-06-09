"""manage gym classes """
from django.db import models
from users.models import CustomUser

class GymClass(models.Model):
    """ list of classes"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.DateTimeField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    """manage booking classes"""
    user_booking = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_booking} - {self.gym_class.name}'