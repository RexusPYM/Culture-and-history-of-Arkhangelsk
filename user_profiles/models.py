from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from historical_objects.models import HistoricalObject


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"


class Comment(models.Model):
    text = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    hist_object = models.ForeignKey(HistoricalObject, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.user.username}. {self.hist_object}. Комментарий: {self.text}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
