""" User model"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from memberships.models import Membership


class CustomUser(AbstractUser):
    """ Creating a new profile user"""
    username = models.CharField('User Name', unique=True, max_length=100)
    email = models.EmailField('Your Email', max_length=254, unique=True)
    name = models.CharField('Your Name', max_length=200, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=200, blank=True, null=True)
    image = models.ImageField(
        default='static/images/profile_images/default.jpg',
        upload_to='static/images/profile_images/',
        )
    user_active = models.BooleanField(default=True)
    current_membership = models.ForeignKey(Membership,on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'name',
        'last_name',
    ]

    def __str__(self):
        return f'User name : {self.name} {self.last_name}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    

