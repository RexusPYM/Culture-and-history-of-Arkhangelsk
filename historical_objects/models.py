from django.db import models
from django.contrib.auth.models import User


class HistoricalObject(models.Model):
    name = models.CharField(max_length=150)
    object_type = models.ForeignKey('ObjectTypes', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    checked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='checked_by')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author')

    def __str__(self):
        return f"{self.name}. {self.description}"[:50]


class TemporaryHistoricalObject(models.Model):
    name = models.CharField(max_length=150)
    object_type = models.ForeignKey('ObjectTypes', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/', null=True, blank=True)


class ProposedHistoricalObject(models.Model):
    name = models.CharField(max_length=150)
    object_type = models.ForeignKey('ObjectTypes', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class ObjectTypes(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Mail(models.Model):
    mail = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.mail}"
