from django.contrib import admin
from .models import Map

# Register your models here.
@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'mode')
    list_filter = ('mode',)
    search_fields = ('mode',)
    fieldsets = (
        ('Basic Information', {'fields':('name', 'icon_name', 'mode')}),
        ('Proficiency Multiplier', {'fields':('proficiency_multiplier',)})
    )