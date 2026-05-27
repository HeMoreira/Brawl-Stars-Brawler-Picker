PROFICIENCIES_PROPERTIES_RELATIONSHIP = {
    'retreat_button': {
        'weaknesses': ['slowness_debuffing'],
        'necessary_against': ['easy_approach'],
        'synergies': ['grass_vision'],
    },
    'wide_attack': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_short_range', 'balance_between_damage_and_durability_in_medium_range','balance_between_damage_and_durability_in_long_range', 'balance_between_damage_and_durability_in_very_long_range',
        ],
        'necessary_against': [
            'multiple_pets_generation', 'durable_pets_generation', 'counter_damage_buffing', 'easy_approach'
        ],
        'synergies': [
            'enemy_position_manipulation', 'shield_buffing', 'area_denial'
        ],
    },
    'area_denial': {
        'weaknesses': [
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range', 'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'enemy_position_manipulation', 'stun_debuffing', 'cover_creation_efficiency', 'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range'
        ],
    },
    'enemy_position_manipulation': {
        'weaknesses': ['retreat_button'],
        'necessary_against': [],
        'synergies': [
            'area_denial', 'wide_attack', 'slowness_debuffing', 'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range'
        ],
    },
    'water_walking': {
        'weaknesses': ['counter_water_walking'],
        'necessary_against': [],
        'synergies': [],
    },
    'counter_water_walking': {
        'weaknesses': [],
        'necessary_against': [],
        'synergies': [],
    },
    'wall_break_efficiency': {
        'weaknesses': [],
        'necessary_against': ['indirect_damage'],
        'synergies': [
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range', 'counter_damage_buffing'
        ],
    },
    'grass_break_efficiency': {
        'weaknesses': [],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range', 'counter_damage_buffing'
        ],
    },
    'cover_creation_efficiency': {
        'weaknesses': [
            'wall_break_efficiency', 'grass_break_efficiency'
        ],
        'necessary_against': [],
        'synergies': [
            'indirect_damage', 'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'grass_vision': {
        'weaknesses': [],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 
            'usual_burst_damage_in_long_range'
        ],
    },
    'circumstantiality_of_overall_proficiency': {
        'weaknesses': [],
        'necessary_against': [],
        'synergies': [],
    },
    'heal_buffing': {
        'weaknesses': ['counter_heal_buffing'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 'balance_between_damage_and_durability_in_medium_range', 'balance_between_damage_and_durability_in_long_range', 'balance_between_damage_and_durability_in_very_long_range', 'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range', 'pressure'
        ],
    },
    'counter_heal_buffing': {
        'weaknesses': [],
        'necessary_against': ['heal_buffing'],
        'synergies': [
            'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range'
        ],
    },
    'shield_buffing': {
        'weaknesses': ['damage_buffing'],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range'
        ],
    },
    'damage_buffing': {
        'weaknesses': [],
        'necessary_against': ['shield_buffing'],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 'balance_between_damage_and_durability_in_medium_range','pressure'
        ],
    },
    'counter_damage_buffing': {
        'weaknesses': [
            'wide_attack', 'retreat_button', 'area_denial'
        ],
        'necessary_against': [],
        'synergies': [
            'pressure', 'balance_between_damage_and_durability_in_short_range', 'balance_between_damage_and_durability_in_medium_range','balance_between_damage_and_durability_in_long_range', 'balance_between_damage_and_durability_in_very_long_range', 'object_burst_damage_in_short_range', 'object_burst_damage_in_medium_range'
        ],
    },
    'speed_buffing': {
        'weaknesses': [
            'wide_attack', 'balance_between_damage_and_durability_in_short_range'
        ],
        'necessary_against': [],
        'synergies': [
            'surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'object_burst_damage_in_short_range', 
            'object_burst_damage_in_medium_range'
        ],
    },
    'invisibility_buffing': {
        'weaknesses': [
            'retreat_button', 'balance_between_damage_and_durability_in_short_range'
        ],
        'necessary_against': [],
        'synergies': [
            'surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range',  'easy_approach', 'pressure'
        ],
    },
    'positioning_buffing': {
        'weaknesses': ['object_burst_damage_in_short_range'],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_short_range', 
            'usual_burst_damage_in_medium_range', 'area_control'
        ],
    },
    'poison_debuffing': {
        'weaknesses': ['counter_poison_debuffing'],
        'necessary_against': [],
        'synergies': ['pressure', 'surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'area_control'],
    },
    'counter_poison_debuffing': {
        'weaknesses': [],
        'necessary_against': ['poison_debuffing'],
        'synergies': [],
    },
    'stun_debuffing': {
        'weaknesses': ['counter_stun_debuffing'],
        'necessary_against': [],
        'synergies': [
            'indirect_damage', 'usual_burst_damage_in_very_long_range', 
            'usual_burst_damage_in_long_range', 'area_denial'
        ],
    },
    'counter_stun_debuffing': {
        'weaknesses': [],
        'necessary_against': ['stun_debuffing'],
        'synergies': [],
    },
    'slowness_debuffing': {
        'weaknesses': ['counter_slowness_debuffing'],
        'necessary_against': [],
        'synergies': [
            'surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 
        ],
    },
    'counter_slowness_debuffing': {
        'weaknesses': [],
        'necessary_against': ['slowness_debuffing'],
        'synergies': [],
    },
    'attacks_canceling': {
        'weaknesses': ['counter_attacks_canceling'],
        'necessary_against': [],
        'synergies': [],
    },
    'counter_attacks_canceling': {
        'weaknesses': [],
        'necessary_against': ['attacks_canceling'],
        'synergies': [],
    },
    'block_enemies': {
        'weaknesses': ['retreat_button'],
        'necessary_against': [],
        'synergies': ['grass_vision'],
    },
    'object_burst_damage_in_short_range': {
        'weaknesses': [
            'usual_burst_damage_in_medium_range', 'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range', 'easy_approach', 'surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 
        ],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'object_burst_damage_in_medium_range': {
        'weaknesses': ['surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure'
        ],
    },
    'object_burst_damage_in_long_range': {
        'weaknesses': ['surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'usual_burst_damage_in_very_long_range', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure'
        ],
    },
    'object_burst_damage_in_very_long_range': {
        'weaknesses': ['easy_approach', 'surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range'],
        'necessary_against': [],
        'synergies': [
            'pressure', 'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range'
        ],
    },
    'usual_burst_damage_in_short_range': {
        'weaknesses': [
            'usual_burst_damage_in_medium_range', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'easy_approach', 'surprise_attack_power_in_very_long_range'
        ],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'usual_burst_damage_in_medium_range': {
        'weaknesses': [
            'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure'
        ],
    },
    'usual_burst_damage_in_long_range': {
        'weaknesses': [
            'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'usual_burst_damage_in_very_long_range', 'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure'
        ],
    },
    'usual_burst_damage_in_very_long_range': {
        'weaknesses': [
            'easy_approach', 'surprise_attack_power_in_very_long_range', 'usual_burst_damage_in_very_long_range', 
        ],
        'necessary_against': [],
        'synergies': [
            'pressure', 'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range'
        ],
    },
    'balance_between_damage_and_durability_in_short_range': {
        'weaknesses': [
            'usual_burst_damage_in_medium_range', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'easy_approach', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range'
        ],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'balance_between_damage_and_durability_in_medium_range': {
        'weaknesses': [
            'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'pressure'
        ],
    },
    'balance_between_damage_and_durability_in_long_range': {
        'weaknesses': [
            'surprise_attack_power_in_very_long_range', 'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'pressure'
        ],
    },
    'balance_between_damage_and_durability_in_very_long_range': {
        'weaknesses': ['easy_approach', 'surprise_attack_power_in_very_long_range'],
        'necessary_against': [],
        'synergies': [
            'pressure', 'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'surprise_attack_power_in_short_range': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_short_range', 'usual_burst_damage_in_medium_range', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 
            'usual_burst_damage_in_short_range', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'retreat_button', 'slowness_debuffing'
        ],
    },
    'surprise_attack_power_in_medium_range': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_short_range', 'usual_burst_damage_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'slowness_debuffing', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'retreat_button'
        ],
    },
    'surprise_attack_power_in_long_range': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_short_range', 'usual_burst_damage_in_short_range', 
            'usual_burst_damage_in_very_long_range', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'slowness_debuffing', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'retreat_button'
        ],
    },
    'surprise_attack_power_in_very_long_range': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_short_range', 'usual_burst_damage_in_short_range', 
            'retreat_button', 'usual_burst_damage_in_very_long_range'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'retreat_button', 'slowness_debuffing', 'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range'
        ],
    },
    'easy_approach': {
        'weaknesses': ['retreat_button', 'wide_attack'],
        'necessary_against': [],
        'synergies': ['slowness_debuffing', 'balance_between_damage_and_durability_in_short_range', 'balance_between_damage_and_durability_in_medium_range', 'balance_between_damage_and_durability_in_long_range', 'balance_between_damage_and_durability_in_very_long_range'],
    },
    'pressure': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_long_range', 
            'balance_between_damage_and_durability_in_very_long_range', 
            'poison_debuffing', 'stun_debuffing', 'slowness_debuffing'
        ],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'counter_poison_debuffing', 'counter_stun_debuffing', 
            'counter_slowness_debuffing', 'heal_buffing'
        ],
    },
    'area_control': {
        'weaknesses': ['usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range'],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_very_long_range', 'usual_burst_damage_in_long_range', 'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'indirect_damage': {
        'weaknesses': ['surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'wall_break_efficiency', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 'balance_between_damage_and_durability_in_medium_range','cover_creation_efficiency', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'multiple_pets_generation': {
        'weaknesses': ['wide_attack', 'groupment_punishment'],
        'necessary_against': [],
        'synergies': ['surprise_attack_power_in_short_range', 'surprise_attack_power_in_medium_range', 'surprise_attack_power_in_long_range', 'surprise_attack_power_in_very_long_range', 'pressure'],
    },
    'durable_pets_generation': {
        'weaknesses': ['groupment_punishment', 'wide_attack'],
        'necessary_against': [],
        'synergies': ['pressure', 'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range'],
    },
    'groupment_punishment': {
        'weaknesses': [],
        'necessary_against': [
            'multiple_pets_generation', 'durable_pets_generation'
        ],
        'synergies': [
            'enemy_position_manipulation', 'pressure', 'indirect_damage', 'easy_approach'
        ],
    }
}