from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from taggit.managers import TaggableManager

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

class Dream(models.Model):
    BLISS = '1'
    GOOD = '2'
    NEUTRAL = '3'
    BAD = '4'
    NIGHTMARE = '5'
    RATING_CHOICES=(
        (BLISS, 'Bliss'),
        (GOOD, 'Good'),
        (NEUTRAL, 'Neutral'),
        (BAD, 'Bad'),
        (NIGHTMARE, 'Nightmare'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=4000)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

class Locations(models.Model):
    dream = models.ManyToManyField(Dream)
    location = TaggableManager()

    def __str__(self):
        return self.location

class Themes(models.Model):
    dream = models.ManyToManyField(Dream)
    theme = TaggableManager()

    def __str__(self):
        return self.theme

post_save.connect(create_profile, sender=User)
