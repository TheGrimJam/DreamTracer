from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

class Dream(models.Model):
    #TODO RATING_CHOICES
    user = models.ManyToOneField(User)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=4000)
    rating = CharField(max_length=1, choices=RATING_CHOICES)
    Locations= #TODO tuples?
    themes= #TODO tuples?

post_save.connect(create_profile, sender=User)
