from brawler.models import Brawler
from django.db import models
from django.forms.models import model_to_dict

PROFICIENCIES_PROPERTIES_RELATIONSHIP = {
    'durability': {
        'weaknesses': [
            'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range', 
            'indirect_damage', 'wall_break_efficiency', 'grass_break_efficiency'
        ],
        'necessary_against': [],
        'synergies': [
            'heal_buffing', 'invisibility_buffing', 'cover_creation_efficiency', 
            'usual_burst_damage_in_very_long_range'
        ],
    },
    'attack_distance': {
        'weaknesses': [
            'attack_distance', 'surprise_attack_power_in_very_long_range', 
            'surprise_attack_power_in_long_range'
        ],
        'necessary_against': [],
        'synergies': [
            'heal_buffing', 'shield_buffing', 'durability', 'counter_damage_buffing'
        ],
    },
    'retreat_button': {
        'weaknesses': ['slowness_debuffing'],
        'necessary_against': ['easy_approach'],
        'synergies': ['_grass_vision'],
    },
    'wide_attack': {
        'weaknesses': ['durability'],
        'necessary_against': [
            'multiple_pets_efficiency', 'durable_pets_efficiency', 
            'counter_damage_buffing', '_movement_speed'
        ],
        'synergies': [
            'enemy_position_manipulation', 'shield_buffing', 'area_denial'
        ],
    },
    'indirect_damage_efficiency': {
        'weaknesses': ['easy_approach', 'wall_break_efficiency'],
        'necessary_against': [],
        'synergies': [
            'cover_creation_efficiency', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'area_denial': {
        'weaknesses': ['attack_distance', 'surprise_attack'],
        'necessary_against': [],
        'synergies': [
            'enemy_position_manipulation', 'stun_debuffing', 
            'cover_creation_efficiency', 'attack_distance'
        ],
    },
    'enemy_position_manipulation': {
        'weaknesses': ['retreat_button'],
        'necessary_against': [],
        'synergies': [
            'area_denial', 'wide_attack', 'slowness_debuffing', 
            'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range'
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
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'counter_damage_buffing', '! indirect_damage'
        ],
    },
    'grass_break_efficiency': {
        'weaknesses': [],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'counter_damage_buffing'
        ],
    },
    'cover_creation_efficiency': {
        'weaknesses': ['wall_break_efficiency', 'grass_break_efficiency'],
        'necessary_against': [],
        'synergies': [
            'indirect_damage', 'balance_between_damage_and_durability_in_short_range'
        ],
    },
    '_movement_speed_': {
        'weaknesses': ['wide_attack'],
        'necessary_against': [],
        'synergies': [],
    },
    '_surprise_attack_power': {
        'weaknesses': [
            'durability', 'retreat_button', 'usual_burst_damage_in_short_range'
        ],
        'necessary_against': [],
        'synergies': [
            'invisibility_buffing', 'counter_damage_buffing', 'shield_buffing'
        ],
    },
    'surprise_attack': {
        'weaknesses': [
            'durability', 'retreat_button', 'usual_burst_damage_in_short_range'
        ],
        'necessary_against': [],
        'synergies': [
            'invisibility_buffing', 'counter_damage_buffing', 'shield_buffing'
        ],
    },
    '_frequency_of_pets_generation': {
        'weaknesses': ['wide_attack'],
        'necessary_against': [],
        'synergies': ['durability'],
    },
    '_accumulation_of_pets': {
        'weaknesses': ['wide_attack'],
        'necessary_against': ['groupment_punishment'],
        'synergies': ['durability'],
    },
    '_deteriorability_of_pets': {
        'weaknesses': ['easy_approach'],
        'necessary_against': [],
        'synergies': [],
    },
    '_pets_resistence': {
        'weaknesses': [
            'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'usual_burst_damage_in_short_range', 
            'easy_approach', 'surprise_attack'
        ],
    },
    '_pets_damage': {
        'weaknesses': ['durability'],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range'
        ],
    },
    '_pets_range': {
        'weaknesses': ['attack_distance'],
        'necessary_against': [],
        'synergies': [],
    },
    '_pets_speed': {
        'weaknesses': ['easy_approach'],
        'necessary_against': [],
        'synergies': ['wide_attack'],
    },
    '_pets_proximity': {
        'weaknesses': ['wide_attack'],
        'necessary_against': ['groupment_punishment'],
        'synergies': ['durability'],
    },
    '_increased_damage_when_grouped': {
        'weaknesses': [],
        'necessary_against': ['multiple_pets_efficiency', 'durable_pets_efficiency'],
        'synergies': [
            'enemy_position_manipulation', 'pressure', 'indirect_damage', 'easy_approach'
        ],
    },
    '_grass_vision': {
        'weaknesses': [],
        'necessary_against': [],
        'synergies': [
            'object_burst_damage_in_short_range', 'object_burst_damage_in_medium_range', 
            'object_burst_damage_in_long_range', 'object_burst_damage_in_very_long_range', 
            'attack_distance'
        ],
    },
    'circumstanciability_of_overall_proficiency': {
        'weaknesses': [],
        'necessary_against': [],
        'synergies': [],
    },
    'heal_buffing': {
        'weaknesses': ['counter_heal_buffing'],
        'necessary_against': [],
        'synergies': ['durability', 'attack_distance', 'pressure'],
    },
    'counter_heal_buffing': {
        'weaknesses': [],
        'necessary_against': ['heal_buffing'],
        'synergies': [
            'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range', 
            'usual_burst_damage_in_long_range', 'usual_burst_damage_in_very_long_range'
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
        'synergies': ['durability', 'pressure'],
    },
    'counter_damage_buffing': {
        'weaknesses': ['wide_attack', 'retreat_button', 'area_denial'],
        'necessary_against': [],
        'synergies': [
            'pressure', 'durability', 'object_burst_damage_in_short_range', 
            'object_burst_damage_in_medium_range'
        ],
    },
    'speed_buffing': {
        'weaknesses': [
            'wide_attack', 'balance_between_damage_and_durability_in_short_range'
        ],
        'necessary_against': [],
        'synergies': [
            'surprise_attack', 'object_burst_damage_in_short_range', 
            'object_burst_damage_in_medium_range'
        ],
    },
    'invisibility_buffing': {
        'weaknesses': [
            'retreat_button', 'balance_between_damage_and_durability_in_short_range'
        ],
        'necessary_against': [],
        'synergies': ['surprise_attack', 'easy_approach', 'pressure'],
    },
    'positioning_buffing': {
        'weaknesses': ['object_burst_damage_in_short_range'],
        'necessary_against': [],
        'synergies': [
            'object_burst_damage_in_short_range', 
            'object_burst_damage_in_medium_range', 'area_control'
        ],
    },
    'poison_debuffing': {
        'weaknesses': ['counter_poison_debuffing'],
        'necessary_against': [],
        'synergies': ['pressure', 'surprise_attack', 'area_control'],
    },
    'counter_poison_debuffing': {
        'weaknesses': [],
        'necessary_against': ['poison_debuffing'],
        'synergies': ['! poison_debuffing'],
    },
    'stun_debuffing': {
        'weaknesses': ['counter_stun_debuffing'],
        'necessary_against': [],
        'synergies': [
            'indirect_damage', 'object_burst_damage_in_very_long_range', 
            'object_burst_damage_in_long_range', 'area_denial'
        ],
    },
    'counter_stun_debuffing': {
        'weaknesses': [],
        'necessary_against': ['stun_debuffing'],
        'synergies': ['! stun_debuffing'],
    },
    'slowness_debuffing': {
        'weaknesses': ['counter_slowness_debuffing'],
        'necessary_against': [],
        'synergies': [
            'surprise_attack', 'object_burst_damage_in_very_long_range', 
            'object_burst_damage_in_long_range'
        ],
    },
    'counter_slowness_debuffing': {
        'weaknesses': [],
        'necessary_against': ['slowness_debuffing'],
        'synergies': ['! slowness_debuffing'],
    },
    'attacks_canceling': {
        'weaknesses': ['counter_attacks_canceling'],
        'necessary_against': [],
        'synergies': ['! counter_attacks_canceling'],
    },
    'counter_attacks_canceling': {
        'weaknesses': [],
        'necessary_against': ['attacks_canceling'],
        'synergies': ['! attacks_canceling'],
    },
    'block_enemies': {
        'weaknesses': ['retreat_button'],
        'necessary_against': [],
        'synergies': ['_grass_vision'],
    },
    'object_burst_damage_in_short_range': {
        'weaknesses': ['attack_distance', 'easy_approach', 'surprise_attack'],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'pressure', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'object_burst_damage_in_medium_range': {
        'weaknesses': ['surprise_attack', 'attack_distance', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'attack_distance', 'pressure'
        ],
    },
    'object_burst_damage_in_long_range': {
        'weaknesses': ['surprise_attack', 'attack_distance', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'attack_distance', 'pressure'
        ],
    },
    'object_burst_damage_in_very_long_range': {
        'weaknesses': ['easy_approach', 'surprise_attack', 'attack_distance'],
        'necessary_against': [],
        'synergies': [
            'pressure', 'balance_between_damage_and_durability_in_short_range', 
            'attack_distance'
        ],
    },
    'usual_burst_damage_in_short_range': {
        'weaknesses': ['attack_distance', 'easy_approach', 'surprise_attack'],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'pressure', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'usual_burst_damage_in_medium_range': {
        'weaknesses': ['surprise_attack', 'attack_distance', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'attack_distance', 'pressure'
        ],
    },
    'usual_burst_damage_in_long_range': {
        'weaknesses': ['surprise_attack', 'attack_distance', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'attack_distance', 'pressure'
        ],
    },
    'usual_burst_damage_in_very_long_range': {
        'weaknesses': ['easy_approach', 'surprise_attack', 'attack_distance'],
        'necessary_against': [],
        'synergies': [
            'pressure', 'balance_between_damage_and_durability_in_short_range', 
            'attack_distance'
        ],
    },
    'balance_between_damage_and_durability_in_short_range': {
        'weaknesses': ['attack_distance', 'easy_approach', 'surprise_attack'],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'pressure', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'balance_between_damage_and_durability_in_medium_range': {
        'weaknesses': ['surprise_attack', 'attack_distance', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'attack_distance', 'pressure'
        ],
    },
    'balance_between_damage_and_durability_in_long_range': {
        'weaknesses': ['surprise_attack', 'attack_distance', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'attack_distance', 'pressure'
        ],
    },
    'balance_between_damage_and_durability_in_very_long_range': {
        'weaknesses': ['easy_approach', 'surprise_attack', 'attack_distance'],
        'necessary_against': [],
        'synergies': [
            'pressure', 'balance_between_damage_and_durability_in_short_range', 
            'attack_distance'
        ],
    },
    'surprise_attack_power_in_short_range': {
        'weaknesses': [
            'durability', 'attack_distance', 
            'usual_burst_damage_in_short_range', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'attack_distance', 'retreat_button', 'slowness_debuffing'
        ],
    },
    'surprise_attack_power_in_medium_range': {
        'weaknesses': [
            'durability', 'usual_burst_damage_in_short_range', 
            'attack_distance', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'slowness_debuffing', 'attack_distance', 'retreat_button'
        ],
    },
    'surprise_attack_power_in_long_range': {
        'weaknesses': [
            'durability', 'usual_burst_damage_in_short_range', 
            'attack_distance', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'slowness_debuffing', 'attack_distance', 'retreat_button'
        ],
    },
    'surprise_attack_power_in_very_long_range': {
        'weaknesses': [
            'durability', 'usual_burst_damage_in_short_range', 
            'retreat_button', 'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range', 
            'retreat_button', 'slowness_debuffing', 'attack_distance'
        ],
    },
    'easy_approach': {
        'weaknesses': ['retreat_button', 'wide_attack'],
        'necessary_against': [],
        'synergies': ['slowness_debuffing', 'durability'],
    },
    'pressure': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_long_range', 
            'balance_between_damage_and_durability_in_very_long_range', 
            'poison_debuffing', 'stun_debuffing', 'slowness_debuffing'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'counter_poison_debuffing', 'counter_stun_debuffing', 
            'counter_slowness_debuffing', 'heal_buffing'
        ],
    },
    'area_control': {
        'weaknesses': ['attack_distance', 'surprise_attack'],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'indirect_damage': {
        'weaknesses': ['surprise_attack', 'wall_break_efficiency', 'easy_approach'],
        'necessary_against': [],
        'synergies': [
            'durability', 'cover_creation_efficiency', 
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'multiple_pets_efficiency': {
        'weaknesses': ['wide_attack', 'groupment_punishment'],
        'necessary_against': [],
        'synergies': ['surprise_attack', 'pressure'],
    },
    'durable_pets_efficiency': {
        'weaknesses': ['groupment_punishment', 'wide_attack'],
        'necessary_against': [],
        'synergies': ['pressure', 'usual_burst_damage_in_short_range', 'usual_burst_damage_in_medium_range'],
    },
    'groupment_punishment': {
        'weaknesses': [],
        'necessary_against': [
            'attack_distance', 'multiple_pets_efficiency', 'durable_pets_efficiency'
        ],
        'synergies': [
            'enemy_position_manipulation', 'pressure', 'indirect_damage', 'easy_approach'
        ],
    }
}


def analyze_all_cards(all_cards):
    results = []
    brawlers_proficiencies = {
        0 : {}, 1 : {}, 2 : {},
        3 : {}, 4 : {}, 5 : {},
    }
    for card in all_cards:
        brawlers_proficiencies[card['index']] = get_brawler_proficiency(card)
    
    for brawler_key, _ in brawlers_proficiencies.items():
        if find_brawler(all_cards[brawler_key]['name']) == None:
            results.append(return_invalid_brawler(brawler_key))
            continue

        convert_proficiencies(brawlers_proficiencies[brawler_key])

        brawlers_proficiencies[brawler_key] = generate_more_properties(brawlers_proficiencies[brawler_key])

        quality_vs_enemies = calculate_quality_vs_enemies(all_cards[brawler_key], brawlers_proficiencies)
        rating = calculate_card_rating(quality_vs_enemies)
        status = calculate_card_status_from_rating(rating)

        results.append({
            'index': brawler_key,
            'status': status,
            'rating': rating,
            'quality_vs_enemies': quality_vs_enemies,
        })

    return results

def get_brawler_proficiency(card):
    brawler = find_brawler(card['name'])
    if not brawler:
        return {}
    brawler_total_proficiency = get_brawler_total_proficiency(brawler, card)
    return brawler_total_proficiency

def get_brawler_total_proficiency(brawler, card):
    dictionary_base_proficiencies = model_to_dict(brawler.base_proficiency)
    total_proficiency = dictionary_base_proficiencies

    selected_gadget = find_gadget(brawler.name, card['gadget_id'])
    selected_starpower = find_starpower(brawler.name, card['starpower_id'])

    if selected_gadget:
        dictionary_gadget_proficiencies = model_to_dict(selected_gadget.base_proficiency)
        for key, value in dictionary_gadget_proficiencies.items():
            total_proficiency[key] += value

    if selected_starpower:
        dictionary_starpower_proficiencies = model_to_dict(selected_starpower.base_proficiency)
        for key, value in dictionary_starpower_proficiencies.items():
            total_proficiency[key] += value

    return total_proficiency

def find_brawler(name):
    if not name:
        return None
    return Brawler.objects.filter(name__iexact=name.strip()).first()

def find_gadget(brawler_name, index):
    brawler = find_brawler(brawler_name)
    if not brawler_name or index not in [1, 2]:
        return None
    elif index == 1:
        return brawler.first_gadget
    else:
        return brawler.second_gadget
    
def find_starpower(brawler_name, index):
    brawler = find_brawler(brawler_name)
    if not brawler_name or index not in [1, 2]:
        return None
    elif index == 1:
        return brawler.first_starpower
    else:
        return brawler.second_starpower




def convert_proficiencies(brawler_proficiencies):
    for key, value in brawler_proficiencies.items():
        brawler_proficiencies[key] = value/10
    return brawler_proficiencies

def generate_more_properties(bp):

    # BASIC DAMAGE PROPERTIES
    bp['object_burst_damage_in_short_range'] = round((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_short_range'] + (bp['ocasional_damage'] / 4), 2)
    bp['object_burst_damage_in_medium_range'] = round((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_medium_range'] + (bp['ocasional_damage'] / 4), 2)
    bp['object_burst_damage_in_long_range'] = round((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_long_range'] + (bp['ocasional_damage'] / 4), 2)
    bp['object_burst_damage_in_very_long_range'] = round((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_very_long_range'] + (bp['ocasional_damage'] / 4), 2)
    bp['usual_burst_damage_in_short_range'] = round(((bp['projectiles_per_shot_in_short_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_short_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * bp['super_damage_in_short_range'])) / (1.25 - ((bp['projectiles_per_shot_in_short_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4), 2)
    bp['usual_burst_damage_in_medium_range'] = round(((bp['projectiles_per_shot_in_medium_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_medium_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * (bp['super_damage_in_medium_range'] - bp['average_super_damage']))) / (1.25 - ((bp['projectiles_per_shot_in_medium_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4), 2)
    bp['usual_burst_damage_in_long_range'] = round(((bp['projectiles_per_shot_in_long_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_long_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * (bp['super_damage_in_long_range'] - bp['average_super_damage']))) / (1.25 - ((bp['projectiles_per_shot_in_long_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4), 2)
    bp['usual_burst_damage_in_very_long_range'] = round(((bp['projectiles_per_shot_in_very_long_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_very_long_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * (bp['super_damage_in_very_long_range'] - bp['average_super_damage']))) / (1.25 - ((bp['projectiles_per_shot_in_very_long_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4), 2)

    # DAMAGE/DURABILITY RELATIONSHIP PROPERTIES
    bp['balance_between_damage_and_durability_in_short_range'] = round(((bp['usual_burst_damage_in_short_range'] / 2) * (bp['durability'] / 1)) / 2, 2)
    bp['balance_between_damage_and_durability_in_medium_range'] = round(((bp['usual_burst_damage_in_medium_range'] / 1) * (bp['durability'] / 2)) / 2, 2)
    bp['balance_between_damage_and_durability_in_long_range'] = round(((bp['usual_burst_damage_in_long_range'] * 1.5) * (bp['durability'] / 3)) / 2, 2)
    bp['balance_between_damage_and_durability_in_very_long_range'] = round(((bp['usual_burst_damage_in_very_long_range'] * 2) * (bp['durability'] / 4)) / 2, 2)

    # SURPRISE ATTACK POWER PROPERTIES
    bp['surprise_attack_power_in_short_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_short_range']) / 2, 2)
    bp['surprise_attack_power_in_medium_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_medium_range']) / 2, 2)
    bp['surprise_attack_power_in_long_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_long_range']) / 2, 2)
    bp['surprise_attack_power_in_very_long_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_very_long_range']) / 2, 2)

    # OTHER PROPERTIES
    bp['easy_approach'] = round(((bp['surprise_attack'] * 4) + (bp['_movement_speed'] * 2) + (bp['durability'] * 2)) / 6, 2)
    bp['pressure'] = round(((((bp['wide_attack'] + ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range']) / 2) / 4000) / 2) * 4) + (bp['durability'] * 4) + (bp['attack_distance'] * 2) + (bp['easy_approach'] * 2)) / 9, 2)
    bp['area_control'] = round(((bp['area_denial'] * 5) + (((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / 4 / 3000) * 2) + (bp['invisibility_buffing'] * 2)) / 6, 2)

    if bp['_indirect_damage_efficiency'] < 6:
        bp['indirect_damage'] = (bp['_indirect_damage_efficiency'] * bp['average_super_damage']) / 2000
    elif bp['_indirect_damage_efficiency'] < 7:
        bp['indirect_damage'] = bp['_indirect_damage_efficiency'] * ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / 4 / 2000)
    else:
        bp['indirect_damage'] = bp['_indirect_damage_efficiency'] * ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / 4 / 2000) * (bp['average_super_damage'] / 2000)
    bp['indirect_damage'] = round(bp['indirect_damage'] / ((10 - bp['attack_distance'] + 2) / 4), 2)

    bp['multiple_pets_generation'] = round((bp['_frequency_of_pets_generation'] * 4) + ((bp['_pets_resistence'] * 2) / (bp['_deteriorability_of_pets'] + 1)) + (bp['_accumulation_of_pets'] * 4), 2)
    bp['durable_pets_generation'] = round((bp['_pets_resistence'] * 3) + (bp['_frequency_of_pets_generation'] * 3) + ((bp['_pets_damage'] * 2) + (bp['_pets_range'] * 2) + (bp['_pets_speed'] * 2)), 2)
    bp['groupment_punishment'] = round(((bp['wide_attack'] * 2) + (bp['stun_debuffing'] * 1) + (bp['groupment_punishment'] * 3)) / 4.5, 2)

    return bp

def calculate_quality_vs_enemies(brawler_index, brawlers_proficiencies):
    enemy_indexes = get_enemy_indexes(brawler_index)
    quality = {}
    for enemy_index in enemy_indexes:
        


        quality[enemy_index] = "X"
        
    return quality

def get_enemy_indexes(card_index):
    if card_index in [0, 1, 2]:
        return [3, 4, 5]
    else:
        return [0, 1, 2]

def calculate_card_rating(quality_vs_enemies):
    for enemy_index, quality in quality_vs_enemies.items():
        ...
    return 50

def calculate_card_status_from_rating(rating):
    if rating >= 85:
        return 'Great'
    if rating >= 60:
        return 'Good'
    if rating >= 40:
        return 'Ok'
    if rating >= 15:
        return 'Bad'
    return 'Awful'

def return_invalid_brawler(index):
    return {
        'index': index,
        'status': 'Invalid',
        'rating': 0,
        'quality_vs_enemies': {},
    }




def aggregate_team_proficiencies(cards):
    totals = {}
    for card in cards:
        brawler = find_brawler(card['name'])
        if not brawler:
            continue
        merge_proficiency_dicts(totals, get_proficiency_values(brawler.base_proficiency))
    return totals

def get_proficiency_values(proficiency):
    if not proficiency:
        return {}

    values = {}
    for field in proficiency._meta.fields:
        if isinstance(field, (models.IntegerField, models.SmallIntegerField)) and field.name != 'id':
            values[field.name] = getattr(proficiency, field.name, 0) or 0
    return values

def merge_proficiency_dicts(target, source):
    for key, value in source.items():
        target[key] = target.get(key, 0) + value
    return target