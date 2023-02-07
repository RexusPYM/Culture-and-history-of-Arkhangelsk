from django.db import models


class Showplace(models.Model):
    name = models.CharField(max_length=100)
    object_type = models.CharField(default='showplace', max_length=10)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}. {self.description}"
