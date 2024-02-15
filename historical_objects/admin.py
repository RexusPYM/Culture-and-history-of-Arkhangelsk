from django.contrib import admin
from .models import *
from .mail_sender import send_mail


class HistoricalObjectAdmin(admin.ModelAdmin):
    # change_list_template = "admin/historical_objects/change_list.html"

    def save_model(self, request, obj, form, change):
        send_mail(text=f"Добавлен новый исторический объект: {obj.name}",
                  addr_to=Mail.objects.all().values_list('mail', flat=True))
        super().save_model(request, obj, form, change)


admin.site.register(HistoricalObject, HistoricalObjectAdmin)
admin.site.register(ObjectTypes)
admin.site.register(Mail)
admin.site.register(ProposedHistoricalObject)
admin.site.register(TemporaryHistoricalObject)
