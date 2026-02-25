from django.contrib import admin
from .models import Proficiency

# Register your models here.
@admin.register(Proficiency)
class ProficiencyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Attacking, being attacked and manipulating terrain', {
            'fields':('durability', 'counter_durability', 'attack_distance', 'counter_attack_distance', 'surprise_attack', 'counter_surprise_attack', 'easy_approximation', 'counter_easy_approximation', 'retreat_button', 'counter_retreat_button', 'burst_damage', 'counter_burst_damage', 'wide_attack', 'counter_wide_attack', 'multiple_pets', 'counter_multiple_pets', 'durable_pets', 'counter_durable_pets', 'groupment_punishment', 'counter_groupment_punishment', 'objects_burst_damage', 'counter_objects_burst_damage', 'indirect_damage', 'counter_indirect_damage', 'area_denial', 'counter_area_denial', 'water_walking', 'counter_water_walking', 'wall_break_efficiency', 'counter_wall_break_efficiency', 'grass_break_efficiency', 'counter_grass_break_efficiency', 'enemy_position_manipulation', 'counter_enemy_position_manipulation')
        }),
        ('Buffing and Debuffing Brawlers', {
            'fields':('heal_buffing', 'counter_heal_buffing', 'shield_buffing', 'counter_shield_buffing', 'damage_buffing', 'counter_damage_buffing', 'speed_buffing', 'counter_speed_buffing', 'invisibility_buffing', 'counter_invisibility_buffing', 'positioning_buffing', 'counter_positioning_buffing', 'poison_debuffing', 'counter_poison_debuffing', 'stun_debuffing', 'counter_stun_debuffing', 'slowness_debuffing', 'counter_slowness_debuffing', 'block_enemies', 'counter_block_enemies', 'attacks_canceling', 'counter_attacks_canceling')
        })
    )