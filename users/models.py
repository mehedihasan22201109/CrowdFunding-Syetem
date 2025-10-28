from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_pic = models.ImageField(
        upload_to="profile_pics/", default="profile_pics/default.png", blank=True
    )
    USER_TYPE_CHOICES = (
        ("admin", "Admin"),
        ("donor", "Donor"),
        ("campaign_creator", "Campaign Creator"),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
