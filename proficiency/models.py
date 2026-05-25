from django.db import models

# Create your models here.
class Proficiency(models.Model):

    class Meta:
        verbose_name = "Proficiency"
        verbose_name_plural = "Proficiencies"

    # Informações básicas sobre dano
    _necessary_projectiles_to_charge_super = models.SmallIntegerField(verbose_name="Necessary Projectiles to Charge Super", help_text="Number of projectiles necessary to charge super", default=0)
    _necessary_supers_to_charge_hipercharge = models.SmallIntegerField(verbose_name="Necessary Supers to Charge Hipercharge", help_text="Number of supers necessary to charge hipercharge", default=0)
    _projectile_damage = models.IntegerField(verbose_name="Projectile Damage", help_text="Damage of each projectile", default=0)
    _shots_per_five_seconds = models.SmallIntegerField(verbose_name="Shots per 5 seconds", help_text="Number of shots that can be fired in 5 seconds", default=0)
    average_projectiles_per_shot = models.SmallIntegerField(verbose_name="Average Projectiles per Shot", help_text="Average number of projectiles fired in each shot", default=0)
    projectiles_per_shot_in_short_range = models.SmallIntegerField(verbose_name="Projectiles per Shot in Short Range", help_text="Average number of projectiles fired in each shot when the enemy is close", default=0)
    projectiles_per_shot_in_medium_range = models.SmallIntegerField(verbose_name="Projectiles per Shot in Medium Range", help_text="Average number of projectiles fired in each shot when the enemy is at medium distance", default=0)
    projectiles_per_shot_in_long_range = models.SmallIntegerField(verbose_name="Projectiles per Shot in Long Range", help_text="Average number of projectiles fired in each shot when the enemy is far", default=0)
    projectiles_per_shot_in_very_long_range = models.SmallIntegerField(verbose_name="Projectiles per Shot in Very Long Range", help_text="Average number of projectiles fired in each shot when the enemy is very far", default=0)
    _auto_charge_super = models.SmallIntegerField(verbose_name="Auto-Charge Super", help_text="Capacity of charging super without firing projectiles (frequency, power)", default=0)
    super_damage_in_short_range = models.IntegerField(verbose_name="Super Damage in Short Range", help_text="Damage of super when the enemy is close", default=0)
    super_damage_in_medium_range = models.IntegerField(verbose_name="Super Damage in Medium Range", help_text="Damage of super when the enemy is at medium distance", default=0)
    super_damage_in_long_range = models.IntegerField(verbose_name="Super Damage in Long Range", help_text="Damage of super when the enemy is far", default=0)
    super_damage_in_very_long_range = models.IntegerField(verbose_name="Super Damage in Very Long Range", help_text="Damage of super when the enemy is very far", default=0)
    average_super_damage = models.IntegerField(verbose_name="Average Super Damage", help_text="Average damage of super", default=0)
    ocasional_damage = models.IntegerField(verbose_name="Ocasional Damage", help_text="Capacity of dealing damage with ocasional attacks (frequency, power)", default=0)

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
    cover_creation_efficiency = models.SmallIntegerField(verbose_name="Cover-Creation-Efficiency", help_text="Capacity of creating covers with attacks (duration, area, durability)", default=0)
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
    _increased_damage_when_grouped = models.SmallIntegerField(verbose_name="Groupment-Punishment", help_text="Capacity of punishing enemies with other hitboxes around", default=0)
    grass_vision = models.SmallIntegerField(verbose_name="Grass-Vision", help_text="Capacity of seeing enemies hiding in the grass", default=0)
    circumstantiality_of_overall_proficiency = models.SmallIntegerField(verbose_name="Circumstantiality of Overall Proficiency", help_text="Defines in what level this proficiency is dependent of external factors that need humam avaliation/observation", default=0)
    
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
    attacks_canceling = models.SmallIntegerField(verbose_name="Forced-Stopped-Time", help_text="Capacity of cancel delayed attacks", default=0)
    counter_attacks_canceling = models.SmallIntegerField(verbose_name="Counter Forced-Stopped-Time", help_text="Capacity of not being affected by attacks canceling", default=0)

