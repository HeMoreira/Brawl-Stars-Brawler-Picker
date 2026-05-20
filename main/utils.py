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
            'heal_buffing', 'shield_buffing', 'wall_break_efficiency', 
            'grass_break_efficiency', 'usual_burst_damage_in_very_long_range'
        ],
    },
    'attack_distance': {
        'weaknesses': [
            'slowness_debuffing', 'attack_distance', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'heal_buffing', 'grass_vision', 'attack_distance', 'slowness_debuffing'
        ],
    },
    'retreat_button': {
        'weaknesses': [
            'durability', 'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'grass_vision', 'slowness_debuffing', 'retreat_button'
        ],
    },
    'wide_attack': {
        'weaknesses': [
            'easy_approach', 'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'enemy_position_manipulation', 'stun_debuffing', 'retreat_button'
        ],
    },
    'indirect_damage_efficiency': {
        'weaknesses': [
            'attack_distance', 'surprise_attack'
        ],
        'necessary_against': [
            'durable_pets_efficiency'
        ],
        'synergies': [
            'cover_creation_efficiency', 'indirect_damage', 'easy_approach'
        ],
    },
    'area_denial': {
        'weaknesses': [
            'attack_distance', 'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'enemy_position_manipulation', 'area_denial'
        ],
    },
    'enemy_position_manipulation': {
        'weaknesses': [
            'counter_water_walking', 'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'area_denial', 'enemy_position_manipulation'
        ],
    },
    'water_walking': {
        'weaknesses': [
            'wall_break_efficiency'
        ],
        'necessary_against': [],
        'synergies': [],
    },
    'counter_water_walking': {
        'weaknesses': [
            'wide_attack'
        ],
        'necessary_against': [],
        'synergies': [],
    },
    'wall_break_efficiency': {
        'weaknesses': [
            'durability'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance', 'wall_break_efficiency'
        ],
    },
    'grass_break_efficiency': {
        'weaknesses': [
            'durability'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance'
        ],
    },
    'cover_creation_efficiency': {
        'weaknesses': [
            'wide_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'indirect_damage', 'durability', 'cover_creation_efficiency'
        ],
    },
    '_movement_speed_': {
        'weaknesses': [],
        'necessary_against': [
            'groupment_punishment'
        ],
        'synergies': [
            'invisibility_buffing', 'usual_burst_damage_in_short_range', 'slowness_debuffing'
        ],
    },
    'surprise_attack_power': {
        'weaknesses': [
            'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'invisibility_buffing', 'wide_attack', 'counter_slowness_debuffing'
        ],
    },
    'surprise_attack_frequency': {
        'weaknesses': [
            'usual_burst_damage_in_short_range'
        ],
        'necessary_against': [],
        'synergies': [
            'durability'
        ],
    },
    'of_pets_generation': {
        'weaknesses': [
            'durability'
        ],
        'necessary_against': [],
        'synergies': [
            'durability'
        ],
    },
    'accumulation_of_pets': {
        'weaknesses': [
            'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'enemy_position_manipulation'
        ],
    },
    'deteriorability_of_pets': {
        'weaknesses': [
            'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'object_burst_damage_in_short_range'
        ],
    },
    'pets_resistence': {
        'weaknesses': [],
        'necessary_against': [
            'groupment_punishment',
            'multiple_pets_efficiency'
        ],
        'synergies': [
            'durability'
        ],
    },
    'pets_damage': {
        'weaknesses': [],
        'necessary_against': [
            'multiple_pets_efficiency'
        ],
        'synergies': [
            'usual_burst_damage_in_short_range'
        ],
    },
    'pets_range': {
        'weaknesses': [
            'counter_heal_buffing'
        ],
        'necessary_against': [
            'heal_buffing'
        ],
        'synergies': [
            'usual_burst_damage_in_very_long_range'
        ],
    },
    'pets_speed': {
        'weaknesses': [
            'damage_buffing'
        ],
        'necessary_against': [
            'shield_buffing'
        ],
        'synergies': [
            'durability'
        ],
    },
    'pets_proximity': {
        'weaknesses': [
            'wide_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'pressure'
        ],
    },
    'groupment_punishment': {
        'weaknesses': [
            'wide_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'surprise_attack'
        ],
    },
    'grass_vision': {
        'weaknesses': [
            'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'surprise_attack'
        ],
    },
    'circumstanciability_of_overall_proficiency': {
        'weaknesses': [
            'object_burst_damage_in_short_range'
        ],
        'necessary_against': [],
        'synergies': [
            'object_burst_damage_in_short_range'
        ],
    },
    'heal_buffing': {
        'weaknesses': [
            'counter_poison_debuffing'
        ],
        'necessary_against': [
            'poison_debuffing'
        ],
        'synergies': [
            'pressure'
        ],
    },
    'counter_heal_buffing': {
        'weaknesses': [
            'counter_stun_debuffing'
        ],
        'necessary_against': [
            'stun_debuffing'
        ],
        'synergies': [
            'poison_debuffing'
        ],
    },
    'shield_buffing': {
        'weaknesses': [
            'counter_slowness_debuffing'
        ],
        'necessary_against': [
            'slowness_debuffing'
        ],
        'synergies': [
            'indirect_damage'
        ],
    },
    'damage_buffing': {
        'weaknesses': [
            'counter_attacks_canceling'
        ],
        'necessary_against': [
            'attacks_canceling'
        ],
        'synergies': [
            'stun_debuffing'
        ],
    },
    'counter_damage_buffing': {
        'weaknesses': [
            'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'surprise_attack'
        ],
    },
    'speed_buffing': {
        'weaknesses': [
            'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'slowness_debuffing'
        ],
    },
    'invisibility_buffing': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'grass_vision'
        ],
    },
    'positioning_buffing': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance'
        ],
    },
    'poison_debuffing': {
        'weaknesses': [
            'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'counter_poison_debuffing': {
        'weaknesses': [
            'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'stun_debuffing': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'pressure'
        ],
    },
    'counter_stun_debuffing': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance'
        ],
    },
    'slowness_debuffing': {
        'weaknesses': [
            'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'counter_slowness_debuffing': {
        'weaknesses': [
            'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'attacks_canceling': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'pressure'
        ],
    },
    'counter_attacks_canceling': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance'
        ],
    },
    'block_enemies': {
        'weaknesses': [
            'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'object_burst_damage_in_short_range': {
        'weaknesses': [
            'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'object_burst_damage_in_medium_range': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'pressure'
        ],
    },
    'object_burst_damage_in_long_range': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'object_burst_damage_in_very_long_range': {
        'weaknesses': [
            'easy_approach'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'usual_burst_damage_in_short_range': {
        'weaknesses': [
            'durability'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'usual_burst_damage_in_medium_range': {
        'weaknesses': [
            'durability'
        ],
        'necessary_against': [],
        'synergies': [
            'slowness_debuffing'
        ],
    },
    'usual_burst_damage_in_long_range': {
        'weaknesses': [
            'durability'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance'
        ],
    },
    'usual_burst_damage_in_very_long_range': {
        'weaknesses': [
            'durability'
        ],
        'necessary_against': [],
        'synergies': [
            'attack_distance'
        ],
    },
    'balance_between_damage_and_durability_in_short_range': {
        'weaknesses': [
            'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'durability'
        ],
    },
    'balance_between_damage_and_durability_in_medium_range': {
        'weaknesses': [
            'balance_between_damage_and_durability_in_long_range'
        ],
        'necessary_against': [],
        'synergies': [
            'surprise_attack'
        ],
    },
    'balance_between_damage_and_durability_in_long_range': {
        'weaknesses': [
            'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'pressure'
        ],
    },
    'balance_between_damage_and_durability_in_very_long_range': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'enemy_position_manipulation'
        ],
    },
    'surprise_attack_power_in_short_range': {
        'weaknesses': [
            'wide_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'invisibility_buffing'
        ],
    },
    'surprise_attack_power_in_medium_range': {
        'weaknesses': [
            'groupment_punishment'
        ],
        'necessary_against': [],
        'synergies': [
            'shield_buffing'
        ],
    },
    'surprise_attack_power_in_long_range': {
        'weaknesses': [
            'attack_distance'
        ],
        'necessary_against': [],
        'synergies': [
            'shield_buffing'
        ],
    },
    'surprise_attack_power_in_very_long_range': {
        'weaknesses': [
            'usual_burst_damage_in_medium_range'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'easy_approach': {
        'weaknesses': [
            'surprise_attack_power_in_very_long_range'
        ],
        'necessary_against': [
            'easy_approach'
        ],
        'synergies': [
            'stun_debuffing'
        ],
    },
    'pressure': {
        'weaknesses': [],
        'necessary_against': [
            'multiple_pets_efficiency'
        ],
        'synergies': [
            'wide_attack'
        ],
    },
    'area_control': {
        'weaknesses': [
            'wall_break_efficiency'
        ],
        'necessary_against': [],
        'synergies': [
            'counter_damage_buffing'
        ],
    },
    'indirect_damage': {
        'weaknesses': [
            'surprise_attack'
        ],
        'necessary_against': [],
        'synergies': [
            'counter_damage_buffing'
        ],
    },
    'multiple_pets_efficiency': {
        'weaknesses': [
            'grass_break_efficiency'
        ],
        'necessary_against': [],
        'synergies': [
            'balance_between_damage_and_durability_in_short_range'
        ],
    },
    'durable_pets_efficiency': {
        'weaknesses': [
            'retreat_button'
        ],
        'necessary_against': [],
        'synergies': []
    },
    'ggroupment_punishment': {
        'weaknesses': [
            'retreat_button'
        ],
        'necessary_against': [],
        'synergies': [
            'usual_burst_damage_in_short_range'
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
    bp['ggroupment_punishment'] = round(((bp['wide_attack'] * 2) + (bp['stun_debuffing'] * 1) + (bp['groupment_punishment'] * 3)) / 4.5, 2)

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