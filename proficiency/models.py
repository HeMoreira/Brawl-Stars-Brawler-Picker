from django.db import models

# Create your models here.
class Proficiency(models.Model):

    class Meta:
        verbose_name = "Proficiency"
        verbose_name_plural = "Proficiencies"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(durability__gte=0),
                name="durability_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(attack_distance__gte=0),
                name="attack_distance_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(retreat_button__gte=0),
                name="retreat_button_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(wide_attack__gte=0),
                name="wide_attack_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_indirect_damage_efficiency__gte=0),
                name="indirect_damage_efficiency_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(area_denial__gte=0),
                name="area_denial_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(enemy_position_manipulation__gte=0),
                name="enemy_position_manipulation_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(water_walking__gte=0),
                name="water_walking_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_water_walking__gte=0),
                name="counter_water_walking_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(wall_break_efficiency__gte=0),
                name="wall_break_efficiency_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(grass_break_efficiency__gte=0),
                name="grass_break_efficiency_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_movement_speed__gte=0),
                name="movement_speed_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_surprise_attack_power__gte=0),
                name="surprise_attack_power_greater_or_equal_to_0"
            ),            
            models.CheckConstraint(
                condition=models.Q(surprise_attack__gte=0),
                name="surprise_attack_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_frequency_of_pets_generation__gte=0),
                name="frequency_of_pets_generation_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_accumulation_of_pets__gte=0),
                name="accumulation_of_pets_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_deteriorability_of_pets__gte=0),
                name="deteriorability_of_pets_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_pets_resistence__gte=0),
                name="pets_resistence_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_pets_damage__gte=0),
                name="pets_damage_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_pets_range__gte=0),
                name="pets_range_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_pets_speed__gte=0),
                name="pets_speed_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(_pets_proximity__gte=0),
                name="pets_proximity_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(groupment_punishment__gte=0),
                name="groupment_punishment_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(heal_buffing__gte=0),
                name="heal_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_heal_buffing__gte=0),
                name="counter_heal_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(shield_buffing__gte=0),
                name="shield_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(damage_buffing__gte=0),
                name="damage_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_damage_buffing__gte=0),
                name="counter_damage_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(speed_buffing__gte=0),
                name="speed_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(invisibility_buffing__gte=0),
                name="invisibility_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(positioning_buffing__gte=0),
                name="positioning_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(poison_debuffing__gte=0),
                name="poison_debuffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_poison_debuffing__gte=0),
                name="counter_poison_debuffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(stun_debuffing__gte=0),
                name="stun_debuffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_stun_debuffing__gte=0),
                name="counter_stun_debuffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(slowness_debuffing__gte=0),
                name="slowness_debuffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_slowness_debuffing__gte=0),
                name="counter_slowness_debuffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(block_enemies__gte=0),
                name="block_enemies_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_block_enemies__gte=0),
                name="counter_block_enemies_greater_or_equal_to_0"
            ),            
            models.CheckConstraint(
                condition=models.Q(attacks_canceling__gte=0),
                name="attacks_canceling_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_attacks_canceling__gte=0),
                name="counter_attacks_canceling_greater_or_equal_to_0"
            ),
        ]

    # Atacando, sendo atacado e manipulando o campo a seu favor
    durability = models.SmallIntegerField(verbose_name="Durability", help_text="Capacity of absorving damage", default=0)
    attack_distance = models.SmallIntegerField(verbose_name="Attack-Distance", help_text="Capacity of attack from long distances", default=0)
    retreat_button = models.SmallIntegerField(verbose_name="Retreat-Button", help_text="Capacity of escape from dangerous attacks (frequency, (versatility, power))", default=0)
    wide_attack = models.SmallIntegerField(verbose_name="Wide-Attack", help_text="Capacity of covering big areas with attacks", default=0)
    _indirect_damage_efficiency = models.SmallIntegerField(verbose_name="Indirect-Damage-Efficiency", help_text="Frequency of indirect damage", default=0)
    area_denial = models.SmallIntegerField(verbose_name="Area-Denial", help_text="Capacity of create effeck areas that block enemies (duration, area, effect)", default=0)
    enemy_position_manipulation = models.SmallIntegerField(verbose_name="Enemy-Position-Manipulation", help_text="Capacity of manipulating enemies position with attacks", default=0)
    water_walking = models.SmallIntegerField(verbose_name="Water-Walking", help_text="Capacity of walking on water", default=0)
    counter_water_walking = models.SmallIntegerField(verbose_name="Counter Water-Walking", help_text="Capacity of dealing damage to water-walking enemies", default=0)
    wall_break_efficiency = models.SmallIntegerField(verbose_name="Wall-Break-Efficiency", help_text="Capacity of wall destruction", default=0)
    grass_break_efficiency = models.SmallIntegerField(verbose_name="Grass-Break-Efficiency", help_text="Capacity of grass destruction", default=0)
    _movement_speed = models.SmallIntegerField(verbose_name="Movement-Speed", help_text="Capacity of moving fast", default=0)
    _surprise_attack_power = models.SmallIntegerField(verbose_name="Surprise-Attack-Power", help_text="Capacity of dealing more damage on surprise attacks", default=0)
    surprise_attack = models.SmallIntegerField(verbose_name="Surprise-Attack", help_text="Capacity of rushing enemies quickly (frequency, (surprise-attack-distance, velocity))", default=0)
    _frequency_of_pets_generation = models.SmallIntegerField(verbose_name="Frequency of Pet Generation", help_text="Capacity of generating pets/objects", default=0)
    _accumulation_of_pets = models.SmallIntegerField(verbose_name="Accumulation of Pets", help_text="Capacity of keeping pets/objects on the field", default=0)
    _deteriorability_of_pets = models.SmallIntegerField(verbose_name="Deteriorability of Pets", help_text="Capacity of pets/objects to be destroyed by enemies", default=0)
    _pets_resistence = models.SmallIntegerField(verbose_name="Pets Resistência", help_text="Capacity of pets/objects to resist attacks", default=0)
    _pets_damage = models.SmallIntegerField(verbose_name="Pets Damage", help_text="Capacity of pets/objects to deal damage to enemies", default=0)
    _pets_range = models.SmallIntegerField(verbose_name="Pets Range", help_text="Capacity of pets/objects to reach enemies", default=0)
    _pets_speed = models.SmallIntegerField(verbose_name="Pets Speed", help_text="Capacity of pets/objects to reach enemies quickly", default=0)
    _pets_proximity = models.SmallIntegerField(verbose_name="Pets Proximity", help_text="Capacity of pets/objects to be close to allies, helping them to approach enemies", default=0)
    groupment_punishment = models.SmallIntegerField(verbose_name="Groupment-Punishment", help_text="Capacity of punishing enemies with other hitboxes around", default=0)
    
    # Buffs: Suporte e seus counters
    heal_buffing = models.SmallIntegerField(verbose_name="Heal-Buffing", help_text="Capacity of heal allies (frequency, power)", default=0)
    counter_heal_buffing = models.SmallIntegerField(verbose_name="Counter Heal-Buffing", help_text="(duration, power)", default=0)
    shield_buffing = models.SmallIntegerField(verbose_name="Shield-Buffing", help_text="Capacity of summon shields on allies (frequency, power)", default=0)
    damage_buffing = models.SmallIntegerField(verbose_name="Damage-Buffing", help_text="Capacity of increasing allies damage (frequency, power, duration)", default=0)
    counter_damage_buffing = models.SmallIntegerField(verbose_name="Counter Damage-Buffing", help_text="(duration, power)", default=0)
    speed_buffing = models.SmallIntegerField(verbose_name="Speed-Buffing", help_text="Capacity of increasing allies speed (frequency, duration)", default=0)
    invisibility_buffing = models.SmallIntegerField(verbose_name="Invisibility-Buffing", help_text="Capacity of applying invisibility on allies (frequency, duration)", default=0)
    positioning_buffing = models.SmallIntegerField(verbose_name="Positioning-Buffing", help_text="Capacity of increasing allies positioning (no parameters at this moment)", default=0)
    poison_debuffing = models.SmallIntegerField(verbose_name="Poison-Debuffing", help_text="Capacity of dealing continuous damage to enemies", default=0)
    counter_poison_debuffing = models.SmallIntegerField(verbose_name="Counter Poison-Debuffing", help_text="(frequency, power)", default=0)
    stun_debuffing = models.SmallIntegerField(verbose_name="Stun-Debuffing", help_text="Capacity of stun enemies", default=0)
    counter_stun_debuffing = models.SmallIntegerField(verbose_name="Counter Stun-Debuffing", help_text="(frequency, power)", default=0)
    slowness_debuffing = models.SmallIntegerField(verbose_name="Slowness-Debuffing", help_text="Capacity of decreasing enemies speed (frequency, power, duration)", default=0)
    counter_slowness_debuffing = models.SmallIntegerField(verbose_name="Counter Slowness-Debuffing", help_text="(frequency, power)", default=0)
    block_enemies = models.SmallIntegerField(verbose_name="Block-Attacks", help_text="Capacity of neutralizing enemies (no parameters at this moment)", default=0)
    counter_block_enemies = models.SmallIntegerField(verbose_name="Counter Block-Attacks", help_text="Capacity of not being neutralized (no parameters at this moment)", default=0)
    attacks_canceling = models.SmallIntegerField(verbose_name="Forced-Stopped-Time", help_text="Capacity of cancel delayed attacks", default=0)
    counter_attacks_canceling = models.SmallIntegerField(verbose_name="Counter Forced-Stopped-Time", help_text="Capacity of not being affected by attacks canceling", default=0)

