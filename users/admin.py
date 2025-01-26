from django.contrib import admin
from .models import  User, Activity

class PotatoCropAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'date', 'county', 'fertilizer_type', 'irrigation_used', 'notes')
    search_fields = ('county', 'fertilizer_type', 'notes')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    ordering = ('username',)  # Default ordering in the admin panel


admin.site.register(User, UserAdmin)
admin.site.register(Activity)
