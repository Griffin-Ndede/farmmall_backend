from django.contrib import admin
from .models import PotatoCrop, User, CalendarEvent

class PotatoCropAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'date', 'county', 'fertilizer_type', 'irrigation_used', 'notes')
    search_fields = ('county', 'fertilizer_type', 'notes')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    ordering = ('username',)  # Default ordering in the admin panel

class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'crop_name', 'activity', 'start_date')
    search_fields = ('crop_name', 'activity')
    # list_filter = ('start_date')  # Add filtering by dates
    ordering = ('start_date',)  # Default ordering by start_date

admin.site.register(PotatoCrop, PotatoCropAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(CalendarEvent, CalendarEventAdmin)
