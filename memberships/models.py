from django.db import models
from django.contrib.auth.models import User


class Membership(models.Model):
    """Memberships"""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Advantage(models.Model):
    """Membership description"""
    membership = models.ForeignKey(Membership,
                                   related_name='advantages',
                                   on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)