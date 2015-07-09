from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_date', 'end_date')

    class Meta:
        ordering = ('-start_date',)

admin.site.register(Event, EventAdmin)
