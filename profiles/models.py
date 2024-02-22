from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model for maintaining default delivery
    information and order history
    """

    # Choices for the nick_name field in the Entry model
    TITLES = [
        ('Grandmaster', 'Grandmaster'),
        ('King', 'King'),
        ('Queen', 'Queen'),
        ('Rook', 'Rook'),
        ('Bishop', 'Bishop'),
        ('Knight', 'Knight'),
        ('Pawn', 'Pawn'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(null=True, blank=True)
    user_title = models.CharField(max_length=50,default="", choices=TITLES, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update user profile """

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()