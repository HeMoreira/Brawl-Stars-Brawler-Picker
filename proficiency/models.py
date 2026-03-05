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
                condition=models.Q(counter_durability__gte=0),
                name="counter_durability_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(attack_distance__gte=0),
                name="attack_distance_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_attack_distance__gte=0),
                name="counter_attack_distance_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(surprise_attack__gte=0),
                name="surprise_attack_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_surprise_attack__gte=0),
                name="counter_surprise_attack_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(easy_approximation__gte=0),
                name="easy_approximation_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_easy_approximation__gte=0),
                name="counter_easy_approximation_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(burst_damage__gte=0),
                name="burst_damage_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_burst_damage__gte=0),
                name="counter_burst_damage_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(objects_burst_damage__gte=0),
                name="objects_burst_damage_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_objects_burst_damage__gte=0),
                name="counter_objects_burst_damage_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(indirect_damage__gte=0),
                name="indirect_damage_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_indirect_damage__gte=0),
                name="counter_indirect_damage_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(area_denial__gte=0),
                name="area_denial_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_area_denial__gte=0),
                name="counter_area_denial_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(multiple_pets__gte=0),
                name="multiple_pets_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_multiple_pets__gte=0),
                name="counter_multiple_pets_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(durable_pets__gte=0),
                name="durable_pets_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_durable_pets__gte=0),
                name="counter_durable_pets_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(wide_attack__gte=0),
                name="wide_attack_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_wide_attack__gte=0),
                name="counter_wide_attack_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(retreat_button__gte=0),
                name="retreat_button_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_retreat_button__gte=0),
                name="counter_retreat_button_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(wall_break_efficiency__gte=0),
                name="wall_break_efficiency_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_wall_break_efficiency__gte=0),
                name="counter_wall_break_efficiency_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(grass_break_efficiency__gte=0),
                name="grass_break_efficiency_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_grass_break_efficiency__gte=0),
                name="counter_grass_break_efficiency_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(enemy_position_manipulation__gte=0),
                name="enemy_position_manipulation_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_enemy_position_manipulation__gte=0),
                name="counter_enemy_position_manipulation_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(groupment_punishment__gte=0),
                name="groupment_punishment_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_groupment_punishment__gte=0),
                name="counter_groupment_punishment_greater_or_equal_to_0"
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
                condition=models.Q(counter_shield_buffing__gte=0),
                name="counter_shield_buffing_greater_or_equal_to_0"
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
                condition=models.Q(counter_speed_buffing__gte=0),
                name="counter_speed_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(invisibility_buffing__gte=0),
                name="invisibility_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_invisibility_buffing__gte=0),
                name="counter_invisibility_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(positioning_buffing__gte=0),
                name="positioning_buffing_greater_or_equal_to_0"
            ),
            models.CheckConstraint(
                condition=models.Q(counter_positioning_buffing__gte=0),
                name="counter_positioning_buffing_greater_or_equal_to_0"
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
    counter_durability = models.SmallIntegerField(verbose_name="Counter Durability", help_text="(average-damage, (attack-distance, durability))", default=0)
    attack_distance = models.SmallIntegerField(verbose_name="Attack-Distance", help_text="Capacity of attack from long distances", default=0)
    counter_attack_distance = models.SmallIntegerField(verbose_name="Counter Attack-Distance", help_text="(attack-distance, surprise-attack, (durability, average-damage))", default=0)
    surprise_attack = models.SmallIntegerField(verbose_name="Surprise-Attack", help_text="Capacity of rushing enemies quickly (frequency, (surprise-attack-distance, velocity))", default=0)
    counter_surprise_attack = models.SmallIntegerField(verbose_name="Counter Surprise-Attack", help_text="(durability, (burst-damage, potential-of-hitting-on-short-distance))", default=0)
    easy_approximation = models.SmallIntegerField(verbose_name="Easy-Approximation", help_text="Capacity of avoiding attacks and get closer (surprise-attack, (movement-speed, durability))", default=0)
    counter_easy_approximation = models.SmallIntegerField(verbose_name="Counter Easy-Aproximation", help_text="(wide-attack, (burst-damage, durability))", default=0)
    burst_damage = models.SmallIntegerField(verbose_name="Burst-Damage", help_text="Capacity of dealing burst damage", default=0)
    counter_burst_damage = models.SmallIntegerField(verbose_name="Counter Burst-Damage", help_text="(retreat-button, (durability, easy-approximation))", default=0)
    objects_burst_damage = models.SmallIntegerField(verbose_name="Objects-Burst-Damage", help_text="Capacity of dealing burst damage to non-players enemies (object-burst-damage, average-attack-distance)", default=0)
    counter_objects_burst_damage = models.SmallIntegerField(verbose_name="Counter Objects-Burst-Damage", help_text="(burst-damage, durability, attack-distance, surprise-attack)", default=0)
    indirect_damage = models.SmallIntegerField(verbose_name="Indirect-Damage", help_text="Capacity of dealing damage ignoring walls (frequency, (attack-distance, burst-damage))", default=0)
    counter_indirect_damage = models.SmallIntegerField(verbose_name="Counter Indirect-Damage", help_text="(surprise-attack, (easy-approximation, velocity-buffing))", default=0)
    area_denial = models.SmallIntegerField(verbose_name="Area-Denial", help_text="Capacity of create effeck areas that block enemies (duration, area, effect)", default=0)
    counter_area_denial = models.SmallIntegerField(verbose_name="Counter Area-Denial", help_text="(durability, (burst-damage, attack-distance), (surprise-attack, retreat-button))", default=0)
    multiple_pets = models.SmallIntegerField(verbose_name="Multiple-Pets", help_text="Capacity of spawning multiple pets/objects (frequency, quantity)", default=0)
    counter_multiple_pets = models.SmallIntegerField(verbose_name="Counter Multiple-Pets", help_text="(groupment-punishment, (wide-attack, (durable-pets, multiple-pets)))", default=0)
    durable_pets = models.SmallIntegerField(verbose_name="Durable-Pets", help_text="Capacity of spawning durable pets/objects (frequency, (pet-durability, pet-damage, pet-velocity, pet-range))", default=0)
    counter_durable_pets = models.SmallIntegerField(verbose_name="Counter Durable-Pets", help_text="(groupment-punishment, (burst-damage, wide-attack))", default=0)
    wide_attack = models.SmallIntegerField(verbose_name="Wide-Attack", help_text="Capacity of covering big areas with attacks", default=0)
    counter_wide_attack = models.SmallIntegerField(verbose_name="Counter Wide-Attack", help_text="(durability, (10 - multiple-pets, 10 - durable-pets))", default=0)
    retreat_button = models.SmallIntegerField(verbose_name="Retreat-Button", help_text="Capacity of escape from dangerous attacks (frequency, (versatility, power))", default=0)
    counter_retreat_button = models.SmallIntegerField(verbose_name="Counter Retreat-Button", help_text="(easy-approximation, (collateral-effect, stun-capacity))", default=0)
    wall_break_efficiency = models.SmallIntegerField(verbose_name="Wall-Break-Efficiency", help_text="Capacity of wall destruction", default=0)
    counter_wall_break_efficiency = models.SmallIntegerField(verbose_name="Counter Wall-Break-Efficiency", help_text="Capacity of playing well after wall destruction", default=0)
    grass_break_efficiency = models.SmallIntegerField(verbose_name="Grass-Break-Efficiency", help_text="Capacity of grass destruction", default=0)
    counter_grass_break_efficiency = models.SmallIntegerField(verbose_name="Counter Grass-Break-Efficiency", help_text="Capacity of playing well after grass destruction", default=0)
    enemy_position_manipulation = models.SmallIntegerField(verbose_name="Enemy-Position-Manipulation", help_text="Capacity of manipulating enemies position with attacks", default=0)
    counter_enemy_position_manipulation = models.SmallIntegerField(verbose_name="Counter Enemy-Position-Manipulation", help_text="(durability, retreat-button, (burst-damage, enemy-position-manipulation))", default=0)
    groupment_punishment = models.SmallIntegerField(verbose_name="Groupment-Punishment", help_text="Capacity of punishing enemies with other hitboxes around", default=0)
    counter_groupment_punishment = models.SmallIntegerField(verbose_name="Counter Groupment-Punishment", help_text="(attack-distance, (10 - multiple-pets, 10 - durable-pets))", default=0)
    water_walking = models.SmallIntegerField(verbose_name="Water-Walking", help_text="Capacity of walking on water", default=0)
    counter_water_walking = models.SmallIntegerField(verbose_name="Counter Water-Walking", help_text="Capacity of dealing damage to water-walking enemies", default=0)

    # Buffs: Suporte e seus counters
    heal_buffing = models.SmallIntegerField(verbose_name="Heal-Buffing", help_text="Capacity of heal allies (frequency, power)", default=0)
    counter_heal_buffing = models.SmallIntegerField(verbose_name="Counter Heal-Buffing", help_text="(duration, power)", default=0)
    shield_buffing = models.SmallIntegerField(verbose_name="Shield-Buffing", help_text="Capacity of summon shields on allies (frequency, power)", default=0)
    counter_shield_buffing = models.SmallIntegerField(verbose_name="Counter Shield-Buffing", help_text="(duration, power)", default=0)
    damage_buffing = models.SmallIntegerField(verbose_name="Damage-Buffing", help_text="Capacity of increasing allies damage (frequency, power, duration)", default=0)
    counter_damage_buffing = models.SmallIntegerField(verbose_name="Counter Damage-Buffing", help_text="(duration, power)", default=0)
    speed_buffing = models.SmallIntegerField(verbose_name="Speed-Buffing", help_text="Capacity of increasing allies speed (frequency, duration)", default=0)
    counter_speed_buffing = models.SmallIntegerField(verbose_name="Counter Speed-Buffing", help_text="Capacity of confront against speed enemies", default=0)
    invisibility_buffing = models.SmallIntegerField(verbose_name="Invisibility-Buffing", help_text="Capacity of applying invisibility on allies (frequency, duration)", default=0)
    counter_invisibility_buffing = models.SmallIntegerField(verbose_name="Counter Invisibility-Buffing", help_text="(wide-attack, attack-distance)", default=0)
    positioning_buffing = models.SmallIntegerField(verbose_name="Positioning-Buffing", help_text="Capacity of increasing allies positioning (no parameters at this moment)", default=0)
    counter_positioning_buffing = models.SmallIntegerField(verbose_name="Counter Positioning-Buffing", help_text="(burst-damage, groupment-punishment)", default=0)
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

