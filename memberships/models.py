# models.py
from django.db import models

class Membership(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Advantage(models.Model):
    membership = models.ForeignKey(Membership, related_name='advantages', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
