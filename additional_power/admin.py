from django.contrib import admin
from .models import Gadget, StarPower, Hipercharge

# Register your models here.
@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        ('Basic Information', {'fields':('name',)}),
        ('Proficiency', {'fields':('base_proficiency',)}),
    )

@admin.register(StarPower)
class StarPowerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        ('Basic Information', {'fields':('name',)}),
        ('Proficiency', {'fields':('base_proficiency',)}),
    )

@admin.register(Hipercharge)
class HiperchargeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        ('Basic Information', {'fields':('name',)}),
        ('Proficiency', {'fields':('base_proficiency',)}),
    )