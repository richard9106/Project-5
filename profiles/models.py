""" models to manage info user"""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from memberships.models import Membership



# User profile.
class Profile(models.Model):
    """model user information"""
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                )
    first_name = models.CharField(max_length=254, default="Mi Name")
    last_name = models.CharField(max_length=254, default="Mi Last Name")
    image = models.ImageField(
        default='static/images/profile_images/user1.jpg',
        upload_to='static/images/profile_images/',
        )
    email = models.EmailField(max_length=254)
    my_memberships = models.ForeignKey(Membership, on_delete=models.CASCADE, blank=True, null=True)
    create_on = models.DateTimeField(
        auto_now_add=True,
        )
    active = models.BooleanField(default=False)

    class Meta:
        """meta class"""
        ordering = ['-id']

    def __str__(self):
        return f"{self.user} | location: {self.email}"


# create user afert some one create an account
# @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """create the user"""
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)