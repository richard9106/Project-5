""" User model"""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from memberships.models import Membership



class CustomUser(models.Model):
    """ Creating a new custom profile user"""
    username = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                )
    first_name = models.CharField(max_length=254, default="Mi Name")
    last_name = models.CharField(max_length=254, default="Mi Last Name")
    image = models.ImageField(
        default='static/images/profile_images/default.jpg',
        upload_to='static/images/profile_images/',
        )
    email = models.EmailField(max_length=254)
    my_membreships = models.ForeignKey(Membership, on_delete=models.CASCADE)
    my_classes = models.ManyToManyField('classes.GymClass')
    create_on = models.DateTimeField(
        auto_now_add=True,
        )
    is_active = models.BooleanField(default=True)

    class Meta:
        """meta class"""
        ordering = ['-id']

    def __str__(self):
        return f"{self.username} | email:{self.email}"


# create user afert some one create an account
# @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """create the user"""
    if created:
        CustomUser.objects.create(username=instance)


post_save.connect(create_user_profile, sender=User)
