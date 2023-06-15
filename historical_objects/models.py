from django.db import models


class HistoricalObject(models.Model):
    name = models.CharField(max_length=150)
    object_type = models.ForeignKey('ObjectTypes', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}. {self.description}"[:50]


class ObjectTypes(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
