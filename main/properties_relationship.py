"""
Manual básico para os pesos das propriedades dos brawlers:
# 1 -> pouco relevante. A capacidade da característica de resolução do problema não é tão grande e não chega a mudar de forma tão relevante o rumo da maioria das situações.
# 2 -> relevante. A caraterística representa uma característica única de seu grupo e resolve um problema, porém, não chega a ser a única forma de resolver o problema, o que a torna não essencial.
# 4 -> essencial. A característica é a única ou uma das únicas formas de lidar efetivamente com um problema específico, o que a torna essencial contra inimigos com essa característica.
"""

PROFICIENCIES_PROPERTIES_RELATIONSHIP = {
    "retreat_button": {
        "weaknesses": [
            [1, "stun_debuffing"]
        ],
        "necessary_against": [
            [2, "easy_approach"]
        ],
        "synergies": [
            [2, "grass_vision"]
        ]
    },
    "wide_attack": {
        "weaknesses": [
            [1, "balance_between_damage_and_durability_in_short_range"],
            [1, "balance_between_damage_and_durability_in_medium_range"],
            [1, "balance_between_damage_and_durability_in_long_range"]
        ],
        "necessary_against": [
            [4, "multiple_pets_generation"],
            [2, "durable_pets_generation"],
            [1, "easy_approach"]
        ],
        "synergies": [
            [2, "enemy_position_manipulation"],
            [2, "shield_buffing"],
            [2, "area_denial"]
        ]
    },
    "area_denial": {
        "weaknesses": [
            [1, "usual_burst_damage_in_long_range"],
            [1, "usual_burst_damage_in_very_long_range"],
            [1, "easy_approach"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "enemy_position_manipulation"],
            [2, "stun_debuffing"],
            [2, "cover_creation_efficiency"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "usual_burst_damage_in_very_long_range"]
        ]
    },
    "enemy_position_manipulation": {
        "weaknesses": [
            [1, "retreat_button"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "area_denial"],
            [2, "wide_attack"],
            [2, "slowness_debuffing"],
            [2, "usual_burst_damage_in_short_range"],
            [2, "usual_burst_damage_in_medium_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "usual_burst_damage_in_very_long_range"]
        ]
    },
    "water_walking": {
        "weaknesses": [
            [4, "counter_water_walking"]
        ],
        "necessary_against": [],
        "synergies": []
    },
    "counter_water_walking": {
        "weaknesses": [],
        "necessary_against": [
            [4, "water_walking"]
        ],
        "synergies": []
    },
    "wall_break_efficiency": {
        "weaknesses": [
            [2, "cover_creation_efficiency"]
        ],
        "necessary_against": [
            [2, "indirect_damage"]
        ],
        "synergies": [
            [2, "usual_burst_damage_in_long_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "counter_damage_buffing"]
        ]
    },
    "grass_break_efficiency": {
        "weaknesses": [
            [2, "cover_creation_efficiency"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "usual_burst_damage_in_long_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "counter_damage_buffing"]
        ]
    },
    "cover_creation_efficiency": {
        "weaknesses": [
            [4, "wall_break_efficiency"],
            [4, "grass_break_efficiency"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "indirect_damage"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ]
    },
    "grass_vision": {
        "weaknesses": [],
        "necessary_against": [],
        "synergies": [
            [2, "usual_burst_damage_in_short_range"],
            [2, "usual_burst_damage_in_medium_range"],
            [2, "usual_burst_damage_in_long_range"]
        ]
    },
    "circumstantiality_of_overall_proficiency": {
        "weaknesses": [],
        "necessary_against": [],
        "synergies": []
    },
    "heal_buffing": {
        "weaknesses": [
            [2, "counter_heal_buffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "balance_between_damage_and_durability_in_medium_range"],
            [2, "balance_between_damage_and_durability_in_long_range"],
            [2, "balance_between_damage_and_durability_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "pressure"]
        ]
    },
    "counter_heal_buffing": {
        "weaknesses": [],
        "necessary_against": [
            [4, "heal_buffing"]
        ],
        "synergies": [
            [2, "usual_burst_damage_in_short_range"],
            [2, "usual_burst_damage_in_medium_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "usual_burst_damage_in_very_long_range"]
        ]
    },
    "shield_buffing": {
        "weaknesses": [
            [2, "damage_buffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"]
        ]
    },
    "damage_buffing": {
        "weaknesses": [
            [2, "shield_buffing"],
            [1, "counter_damage_buffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "balance_between_damage_and_durability_in_medium_range"],
            [2, "pressure"]
        ]
    },
    "counter_damage_buffing": {
        "weaknesses": [
            [1, "wide_attack"],
            [1, "retreat_button"],
            [1, "area_denial"]
        ],
        "necessary_against": [
            [4, "damage_buffing"]
        ],
        "synergies": [
            [2, "pressure"],
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "balance_between_damage_and_durability_in_medium_range"],
            [2, "balance_between_damage_and_durability_in_long_range"],
            [2, "balance_between_damage_and_durability_in_very_long_range"],
            [2, "object_burst_damage_in_short_range"],
            [2, "object_burst_damage_in_medium_range"]
        ]
    },
    "speed_buffing": {
        "weaknesses": [
            [1, "wide_attack"],
        ],
        "necessary_against": [
            [1, "balance_between_damage_and_durability_in_short_range"]
        ],
        "synergies": [
            [2, "surprise_attack_power_in_short_range"],
            [2, "surprise_attack_power_in_medium_range"],
            [2, "surprise_attack_power_in_long_range"],
            [2, "object_burst_damage_in_short_range"],
            [2, "object_burst_damage_in_medium_range"]
        ]
    },
    "invisibility_buffing": {
        "weaknesses": [
            [1, "retreat_button"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "surprise_attack_power_in_short_range"],
            [2, "surprise_attack_power_in_medium_range"],
            [2, "surprise_attack_power_in_long_range"],
            [2, "easy_approach"],
            [2, "pressure"]
        ]
    },
    "positioning_buffing": {
        "weaknesses": [
            [1, "object_burst_damage_in_short_range"],
            [1, "object_burst_damage_in_medium_range"],
            [1, "object_burst_damage_in_long_range"],
            [1, "object_burst_damage_in_very_long_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "usual_burst_damage_in_short_range"],
            [2, "usual_burst_damage_in_medium_range"],
            [2, "area_control"]
        ]
    },
    "poison_debuffing": {
        "weaknesses": [
            [2, "counter_poison_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "pressure"],
            [2, "surprise_attack_power_in_short_range"],
            [2, "surprise_attack_power_in_medium_range"],
            [2, "surprise_attack_power_in_long_range"],
            [2, "surprise_attack_power_in_very_long_range"],
            [2, "area_control"]
        ]
    },
    "counter_poison_debuffing": {
        "weaknesses": [],
        "necessary_against": [
            [4, "poison_debuffing"]
        ],
        "synergies": []
    },
    "stun_debuffing": {
        "weaknesses": [
            [2, "counter_stun_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "indirect_damage"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "area_denial"]
        ]
    },
    "counter_stun_debuffing": {
        "weaknesses": [],
        "necessary_against": [
            [4, "stun_debuffing"]
        ],
        "synergies": []
    },
    "slowness_debuffing": {
        "weaknesses": [
            [2, "counter_slowness_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "surprise_attack_power_in_short_range"],
            [2, "surprise_attack_power_in_medium_range"],
            [2, "surprise_attack_power_in_long_range"],
            [2, "surprise_attack_power_in_very_long_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"]
        ]
    },
    "counter_slowness_debuffing": {
        "weaknesses": [],
        "necessary_against": [
            [4, "slowness_debuffing"]
        ],
        "synergies": []
    },
    "attacks_canceling": {
        "weaknesses": [
            [2, "counter_attacks_canceling"]
        ],
        "necessary_against": [],
        "synergies": []
    },
    "counter_attacks_canceling": {
        "weaknesses": [],
        "necessary_against": [
            [2, "attacks_canceling"]
        ],
        "synergies": []
    },
    "block_enemies": {
        "weaknesses": [
            [1, "retreat_button"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "grass_vision"]
        ]
    },
    "object_burst_damage_in_short_range": {
        "weaknesses": [
            [1, "usual_burst_damage_in_medium_range"],
            [1, "usual_burst_damage_in_long_range"],
            [1, "usual_burst_damage_in_very_long_range"],
            [2, "pressure"],
            [1, "enemy_position_manipulation"],
            [1, "block_enemies"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ]
    },
    "object_burst_damage_in_medium_range": {
        "weaknesses": [
            [1, "surprise_attack_power_in_long_range"],
            [1, "surprise_attack_power_in_very_long_range"],
            [1, "usual_burst_damage_in_very_long_range"],
            [1, "usual_burst_damage_in_long_range"],
            [1, "pressure"],
            [1, "block_enemies"],
            [1, "enemy_position_manipulation"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"]
        ]
    },
    "object_burst_damage_in_long_range": {
        "weaknesses": [
            [1, "surprise_attack_power_in_long_range"],
            [1, "surprise_attack_power_in_very_long_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [1, "easy_approach"],
            [1, "enemy_position_manipulation"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"]
        ]
    },
    "object_burst_damage_in_very_long_range": {
        "weaknesses": [
            [1, "surprise_attack_power_in_long_range"],
            [1, "surprise_attack_power_in_very_long_range"],
            [1, "easy_approach"],
            [1, "usual_burst_damage_in_very_long_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "pressure"],
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"]
        ]
    },
    "usual_burst_damage_in_short_range": {
        "weaknesses": [
            [4, "retreat_button"],
            [2, "usual_burst_damage_in_medium_range"],
            [3, "usual_burst_damage_in_long_range"],
            [4, "usual_burst_damage_in_very_long_range"],
            [2, "pressure"],
            [2, "block_enemies"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "retreat_button"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ]
    },
    "usual_burst_damage_in_medium_range": {
        "weaknesses": [
            [1, "surprise_attack_power_in_long_range"],
            [1, "surprise_attack_power_in_very_long_range"],
            [3, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"],
            [2, "block_enemies"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"]
        ]
    },
    "usual_burst_damage_in_long_range": {
        "weaknesses": [
            [2, "surprise_attack_power_in_long_range"],
            [2, "surprise_attack_power_in_very_long_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [4, "easy_approach"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"]
        ]
    },
    "usual_burst_damage_in_very_long_range": {
        "weaknesses": [
            [2, "surprise_attack_power_in_long_range"],
            [2, "surprise_attack_power_in_very_long_range"],
            [4, "easy_approach"],
            [1, "usual_burst_damage_in_very_long_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "pressure"],
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"]
        ]
    },
    "balance_between_damage_and_durability_in_short_range": {
        "weaknesses": [
            [2, "usual_burst_damage_in_medium_range"],
            [4, "usual_burst_damage_in_very_long_range"],
            [3, "usual_burst_damage_in_long_range"],
            [2, "pressure"]
        ],
        "necessary_against": [
            [4, "surprise_attack_power_in_medium_range"],
            [4, "surprise_attack_power_in_long_range"],
            [4, "surprise_attack_power_in_very_long_range"]
        ],
        "synergies": [
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ]
    },
    "balance_between_damage_and_durability_in_medium_range": {
        "weaknesses": [
            [3, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "pressure"]
        ]
    },
    "balance_between_damage_and_durability_in_long_range": {
        "weaknesses": [
            [2, "surprise_attack_power_in_very_long_range"],
            [2, "surprise_attack_power_in_long_range"],
            [4, "easy_approach"],
            [2, "usual_burst_damage_in_very_long_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "pressure"]
        ]
    },
    "balance_between_damage_and_durability_in_very_long_range": {
        "weaknesses": [
            [2, "easy_approach"],
            [2, "surprise_attack_power_in_very_long_range"],
            [2, "surprise_attack_power_in_long_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "pressure"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ]
    },
    "surprise_attack_power_in_short_range": {
        "weaknesses": [
            [4, "balance_between_damage_and_durability_in_short_range"],
            [3, "usual_burst_damage_in_short_range"],
            [1, "retreat_button"],
            [3, "enemy_position_manipulation"],
            [1, "block_enemies"],
            [2, "stun_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "retreat_button"],
            [2, "slowness_debuffing"]
        ]
    },
    "surprise_attack_power_in_medium_range": {
        "weaknesses": [
            [4, "balance_between_damage_and_durability_in_short_range"],
            [3, "usual_burst_damage_in_short_range"],
            [2, "retreat_button"],
            [3, "enemy_position_manipulation"],
            [1, "block_enemies"],
            [2, "stun_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "slowness_debuffing"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "retreat_button"]
        ]
    },
    "surprise_attack_power_in_long_range": {
        "weaknesses": [
            [4, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_short_range"],
            [3, "retreat_button"],
            [2, "enemy_position_manipulation"],
            [2, "block_enemies"],
            [3, "stun_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "slowness_debuffing"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "retreat_button"]
        ]
    },
    "surprise_attack_power_in_very_long_range": {
        "weaknesses": [
            [4, "balance_between_damage_and_durability_in_short_range"],
            [2, "usual_burst_damage_in_short_range"],
            [3, "retreat_button"],
            [2, "enemy_position_manipulation"],
            [2, "block_enemies"],
            [3, "stun_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "retreat_button"],
            [2, "slowness_debuffing"],
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"]
        ]
    },
    "easy_approach": {
        "weaknesses": [
            [2, "retreat_button"],
            [1, "wide_attack"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "slowness_debuffing"],
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "balance_between_damage_and_durability_in_medium_range"],
            [2, "balance_between_damage_and_durability_in_long_range"],
            [2, "balance_between_damage_and_durability_in_very_long_range"]
        ]
    },
    "pressure": {
        "weaknesses": [
            [4, "usual_burst_damage_in_very_long_range"],
            [3, "usual_burst_damage_in_long_range"],
            [2, "poison_debuffing"],
            [1, "stun_debuffing"],
            [2, "slowness_debuffing"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "counter_poison_debuffing"],
            [2, "counter_stun_debuffing"],
            [2, "counter_slowness_debuffing"],
            [2, "heal_buffing"]
        ]
    },
    "area_control": {
        "weaknesses": [
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "surprise_attack_power_in_short_range"],
            [2, "surprise_attack_power_in_medium_range"],
            [2, "surprise_attack_power_in_long_range"],
            [2, "surprise_attack_power_in_very_long_range"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "usual_burst_damage_in_very_long_range"],
            [2, "usual_burst_damage_in_long_range"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ]
    },
    "indirect_damage": {
        "weaknesses": [
            [2, "surprise_attack_power_in_short_range"],
            [2, "surprise_attack_power_in_medium_range"],
            [2, "surprise_attack_power_in_long_range"],
            [2, "surprise_attack_power_in_very_long_range"],
            [4, "wall_break_efficiency"],
            [4, "easy_approach"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "balance_between_damage_and_durability_in_short_range"],
            [2, "balance_between_damage_and_durability_in_medium_range"],
            [2, "cover_creation_efficiency"],
            [2, "balance_between_damage_and_durability_in_short_range"]
        ]
    },
    "multiple_pets_generation": {
        "weaknesses": [
            [4, "wide_attack"],
            [3, "groupment_punishment"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "surprise_attack_power_in_short_range"],
            [2, "surprise_attack_power_in_medium_range"],
            [2, "surprise_attack_power_in_long_range"],
            [2, "surprise_attack_power_in_very_long_range"],
            [2, "pressure"]
        ]
    },
    "durable_pets_generation": {
        "weaknesses": [
            [4, "groupment_punishment"],
            [3, "wide_attack"]
        ],
        "necessary_against": [],
        "synergies": [
            [2, "pressure"],
            [2, "usual_burst_damage_in_short_range"],
            [2, "usual_burst_damage_in_medium_range"]
        ]
    },
    "groupment_punishment": {
        "weaknesses": [],
        "necessary_against": [
            [3, "multiple_pets_generation"],
            [4, "durable_pets_generation"]
        ],
        "synergies": [
            [2, "enemy_position_manipulation"],
            [2, "pressure"],
            [2, "indirect_damage"],
            [2, "easy_approach"]
        ]
    }
}