from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_donated = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)

    def __str__(self):
        return self.event_name


class Purchase(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, related_name="purchases")
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    with_driver = models.BooleanField(default=False)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    @property
    def driver_fee(self):
        return 4000 if self.with_driver else 0

    def __str__(self):
        return f"{self.user.username} purchased {self.event.event_name}"
