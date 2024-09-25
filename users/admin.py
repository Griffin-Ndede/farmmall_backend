from django.contrib import admin
from .models import PotatoCrop

class PotatoCropAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'date', 'county', 'fertilizer_type', 'irrigation_used', 'notes')
    search_fields = ('county', 'fertilizer_type', 'notes')

admin.site.register(PotatoCrop, PotatoCropAdmin)
