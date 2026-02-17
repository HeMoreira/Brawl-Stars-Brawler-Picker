from django.contrib import admin
from .models import Brawler

# Register your models here.
@admin.register(Brawler)
class BrawlerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'primary_class', 'secondary_class')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'primary_class', 'secondary_class')
        }),
        ('Gadgets, Star Powers and Hipercharges', {
            'fields':('first_gadget', 'second_gadget', 'first_starpower', 'second_starpower', 'hipercharge')
        }),
        ('Base Proficiency', {
            'fields':('base_proficiency',)
        }),
    )