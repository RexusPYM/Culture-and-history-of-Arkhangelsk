from django.contrib import admin
from .models import HistoricalObject, ObjectTypes

admin.site.register(HistoricalObject)
admin.site.register(ObjectTypes)
