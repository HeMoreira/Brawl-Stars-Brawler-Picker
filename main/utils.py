from brawler.models import Brawler
from django.db import models
from django.forms.models import model_to_dict
from .properties_relationship import PROFICIENCIES_PROPERTIES_RELATIONSHIP

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
        brawlers_proficiencies[brawler_key] = get_final_brawler_properties(brawlers_proficiencies[brawler_key])
    
    for brawler_key, _ in brawlers_proficiencies.items():
        if find_brawler(all_cards[brawler_key]['name']) == None:
            results.append(return_invalid_brawler(brawler_key))
            continue

        quality_vs_enemies = calculate_quality_vs_enemies(all_cards[brawler_key]['index'], brawlers_proficiencies)
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

def get_final_brawler_properties(bp):

    weight_object_burst_damage_isr = 2000
    weight_object_burst_damage_imr = 1800
    weight_object_burst_damage_ilr = 1750
    weight_object_burst_damage_ivlr = 1650

    weight_usual_burst_damage_isr = 1800
    weight_usual_burst_damage_imr = 1000
    weight_usual_burst_damage_ilr = 500
    weight_usual_burst_damage_ivlr = 170

    # BASIC DAMAGE PROPERTIES
    bp['object_burst_damage_in_short_range'] = round(((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_short_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_isr, 2)
    bp['object_burst_damage_in_medium_range'] = round(((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_medium_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_imr, 2)
    bp['object_burst_damage_in_long_range'] = round(((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_long_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_ilr, 2)
    bp['object_burst_damage_in_very_long_range'] = round(((bp['average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_very_long_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_ivlr, 2)
    bp['usual_burst_damage_in_short_range'] = round((((bp['projectiles_per_shot_in_short_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_short_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * bp['super_damage_in_short_range'])) / (1.25 - ((bp['projectiles_per_shot_in_short_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_isr, 2)
    bp['usual_burst_damage_in_medium_range'] = round((((bp['projectiles_per_shot_in_medium_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_medium_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * (bp['super_damage_in_medium_range'] - bp['average_super_damage']))) / (1.25 - ((bp['projectiles_per_shot_in_medium_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_imr, 2)
    bp['usual_burst_damage_in_long_range'] = round((((bp['projectiles_per_shot_in_long_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_long_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * (bp['super_damage_in_long_range'] - bp['average_super_damage']))) / (1.25 - ((bp['projectiles_per_shot_in_long_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_ilr, 2)
    bp['usual_burst_damage_in_very_long_range'] = round((((bp['projectiles_per_shot_in_very_long_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['projectiles_per_shot_in_very_long_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * (bp['super_damage_in_very_long_range'] - bp['average_super_damage']))) / (1.25 - ((bp['projectiles_per_shot_in_very_long_range'] - bp['average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_ivlr, 2)
    if bp['usual_burst_damage_in_very_long_range'] < 0:
        bp['usual_burst_damage_in_very_long_range'] = 0

    # DAMAGE/DURABILITY RELATIONSHIP PROPERTIES
    bp['balance_between_damage_and_durability_in_short_range'] = round(((bp['usual_burst_damage_in_short_range'] / 2) * (bp['durability'] / 1)) / 2.5, 2)
    bp['balance_between_damage_and_durability_in_medium_range'] = round(((bp['usual_burst_damage_in_medium_range'] / 1) * (bp['durability'] / 2)) / 3, 2)
    bp['balance_between_damage_and_durability_in_long_range'] = round(((bp['usual_burst_damage_in_long_range'] * 1.5) * (bp['durability'] / 3)) / 2.5, 2)
    bp['balance_between_damage_and_durability_in_very_long_range'] = round(((bp['usual_burst_damage_in_very_long_range'] * 2) * (bp['durability'] / 4.5)) / 4, 2)

    # SURPRISE ATTACK POWER PROPERTIES
    bp['surprise_attack_power_in_short_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_short_range']) / 3, 2)
    bp['surprise_attack_power_in_medium_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_medium_range']) / 2.7, 2)
    bp['surprise_attack_power_in_long_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_long_range']) / 2.4, 2)
    bp['surprise_attack_power_in_very_long_range'] = round((bp['surprise_attack'] * bp['balance_between_damage_and_durability_in_very_long_range']) / 1.9, 2)

    # OTHER PROPERTIES
    bp['easy_approach'] = round(((bp['surprise_attack'] * 4) + (bp['_movement_speed'] * 2) + (bp['durability'] * 2)) / 6, 2)
    bp['pressure'] = round(((((bp['wide_attack'] + ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range']) / 2) / 1.5) / 2) * 4) + (bp['durability'] * 4) + (bp['attack_distance'] * 2) + (bp['easy_approach'] * 2)) / 9, 2)
    bp['area_control'] = round(((bp['area_denial'] * 5) + (((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / (4 * 2)) * 2) + (bp['invisibility_buffing'] * 2)) / 6, 2)

    if bp['_indirect_damage_efficiency'] < 6:
        bp['indirect_damage'] = (bp['_indirect_damage_efficiency'] * bp['average_super_damage']) / 2000
    elif bp['_indirect_damage_efficiency'] < 7:
        bp['indirect_damage'] = bp['_indirect_damage_efficiency'] * ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / (4 * 2.5))
    else:
        bp['indirect_damage'] = bp['_indirect_damage_efficiency'] * ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / (4 * 2.5)) * (bp['average_super_damage'] / 2000)
    bp['indirect_damage'] = round(bp['indirect_damage'] / ((10 - bp['attack_distance'] + 2) / 4), 2)

    bp['multiple_pets_generation'] = round((bp['_frequency_of_pets_generation'] * 4) + ((bp['_pets_resistence'] * 2) / (bp['_deteriorability_of_pets'] + 1)) + (bp['_accumulation_of_pets'] * 4), 2)
    bp['durable_pets_generation'] = round((bp['_pets_resistence'] * 3) + (bp['_frequency_of_pets_generation'] * 3) + ((bp['_pets_damage'] * 2) + (bp['_pets_range'] * 2) + (bp['_pets_speed'] * 2)), 2)
    bp['groupment_punishment'] = round(((bp['wide_attack'] * 2) + (bp['stun_debuffing'] * 1) + (bp['_increased_damage_when_grouped'] * 3)) / 4.5, 2)

    del bp['durability']
    del bp['attack_distance']
    del bp['surprise_attack']
    properties_to_delete = []
    for property_key in bp.keys():
        if property_key[0] == '_':
            properties_to_delete.append(property_key)
    for property_name in properties_to_delete:
        del bp[property_name]

    print(bp, "\n\n\n")

    return bp

def calculate_quality_vs_enemies(brawler_index, brawlers_proficiencies):
    enemy_indexes = get_enemy_indexes(brawler_index)
    quality = {}
    for enemy_index in enemy_indexes:
        quality[enemy_index] = 0
        for property_key in brawlers_proficiencies[enemy_index].keys():
            if property_key in ['id', '_necessary_projectiles_to_charge_super', '_necessary_supers_to_charge_hipercharge', '_projectile_damage', '_shots_per_five_seconds', 'average_projectiles_per_shot', 'projectiles_per_shot_in_short_range', 'projectiles_per_shot_in_medium_range', 'projectiles_per_shot_in_long_range', 'projectiles_per_shot_in_very_long_range', '_auto_charge_super', 'super_damage_in_short_range', 'super_damage_in_medium_range', 'super_damage_in_long_range', 'super_damage_in_very_long_range', 'average_super_damage', 'ocasional_damage']:
                continue
            analized_brawler_power_values = []
            property_relations = PROFICIENCIES_PROPERTIES_RELATIONSHIP[property_key]

            analized_brawler_properties = brawlers_proficiencies[brawler_index]
            analized_enemy_properties = brawlers_proficiencies[enemy_index]

            print(property_key, ":", analized_brawler_properties[property_key])

            for weakness in property_relations['weaknesses']:
                result = result = (((analized_brawler_properties[property_key] - analized_enemy_properties[weakness]) * (analized_brawler_properties[property_key])) / 10) - ((analized_enemy_properties[weakness] * analized_brawler_properties[property_key]) / 10)
                analized_brawler_power_values.append(result)
                print("property:", weakness, analized_enemy_properties[weakness], result)

            for necessity in property_relations['necessary_against']:
                result = analized_brawler_properties[property_key] + (analized_enemy_properties[necessity] * -1)
                if result < 0:
                    analized_brawler_power_values.append(result)
                else:
                    analized_brawler_power_values.append(0)
                print("necessity:", necessity, analized_enemy_properties[necessity], result)

            print("\n\n", analized_brawler_power_values, quality[enemy_index], "\n\n")

            result_analized_brawler = 0
            for power in analized_brawler_power_values:
                result_analized_brawler += power
            result_analized_brawler /= len(analized_brawler_power_values)+1

            quality[enemy_index] += result_analized_brawler
            
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