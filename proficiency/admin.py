from django.contrib import admin
from .models import Proficiency

# Register your models here.
@admin.register(Proficiency)
class ProficiencyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Damage Information', {
            'fields':(
                '_necessary_projectiles_to_charge_super',
                '_necessary_supers_to_charge_hipercharge',
                '_projectile_damage',
                '_shots_per_five_seconds',
                '_average_projectiles_per_shot',
                '_projectiles_per_shot_in_short_range',
                '_projectiles_per_shot_in_medium_range',
                '_projectiles_per_shot_in_long_range',
                '_projectiles_per_shot_in_very_long_range',
                '_shotting_time',
                '_auto_charge_super',
                'super_damage_in_short_range',
                'super_damage_in_medium_range',
                'super_damage_in_long_range',
                'super_damage_in_very_long_range',
                'average_super_damage',
                '_super_time',
                'ocasional_damage',
            )
        }),
        ('Attacking, being attacked and manipulating terrain', {
            'fields':(
                '_durability',
                '_attack_distance',
                'retreat_button',
                'wide_attack',
                '_indirect_damage_efficiency',
                'area_denial',
                'enemy_position_manipulation',
                'water_walking',
                'counter_water_walking',
                'wall_break_efficiency',
                'grass_break_efficiency',
                'cover_creation_efficiency',
                '_movement_speed',
                '_surprise_attack_power',
                '_surprise_attack',
                '_frequency_of_pets_generation',
                '_accumulation_of_pets',
                '_deteriorability_of_pets',
                '_pets_resistence',
                '_pets_damage',
                '_pets_range',
                '_pets_speed',
                '_pets_proximity',
                '_increased_damage_when_grouped',
                'grass_vision',
                'circumstantiality_of_overall_proficiency',
                'explanation_for_circumstantiality',
            )
        }),
        ('Buffs and Debuffs', {
            'fields':(
                'heal_buffing',
                'counter_heal_buffing',
                'shield_buffing',
                'damage_buffing',
                'counter_damage_buffing',
                'speed_buffing',
                'invisibility_buffing',
                'positioning_buffing',
                'poison_debuffing',
                'counter_poison_debuffing',
                'stun_debuffing',
                'counter_stun_debuffing',
                'slowness_debuffing',
                'counter_slowness_debuffing',
                'block_enemies',
                'attacks_canceling',
                'counter_attacks_canceling',
            )
        }),
        ('Specific Weaknesses', {
            'fields':(
                'main_specific_weakness',
                'specific_weakness',
            )
        }),
    )
