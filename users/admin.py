from django.contrib import admin
from .models import PotatoCrop

class PotatoCropAdmin(admin.ModelAdmin):
    list_display = ('id', 'planting_date', 'region', 'fertilizer_type', 'irrigation_used', 'notes')
    search_fields = ('region', 'fertilizer_type', 'notes')

admin.site.register(PotatoCrop, PotatoCropAdmin)
