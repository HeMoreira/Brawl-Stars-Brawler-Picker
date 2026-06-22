from brawler.models import Brawler
from django.db import models
from django.forms.models import model_to_dict
from .properties_relationship import PROFICIENCIES_PROPERTIES_RELATIONSHIP

def analyze_all_cards(all_cards):
    results = [
        {"quality_vs_enemies":{}}, {"quality_vs_enemies":{}}, {"quality_vs_enemies":{}}, 
        {"quality_vs_enemies":{}}, {"quality_vs_enemies":{}}, {"quality_vs_enemies":{}}
    ]
    brawlers_proficiencies = {
        0 : {}, 1 : {}, 2 : {},
        3 : {}, 4 : {}, 5 : {},
    }
    for card in all_cards:
        brawlers_proficiencies[card['index']] = get_brawler_proficiency(card)

    for brawler_key, _ in brawlers_proficiencies.items():
        if find_brawler(all_cards[brawler_key]['name']) == None:
            results[brawler_key] = return_invalid_brawler(brawler_key)
            continue
        convert_proficiencies(brawlers_proficiencies[brawler_key])
        brawlers_proficiencies[brawler_key] = get_final_brawler_properties(brawlers_proficiencies[brawler_key])
    
    for brawler_key, _ in brawlers_proficiencies.items():
        if brawler_key < 3:
            if find_brawler(all_cards[brawler_key]['name']) == None:
                results[brawler_key] = return_invalid_brawler(brawler_key)
                continue

            quality_vs_enemies = calculate_quality_vs_enemies(all_cards[brawler_key]['index'], brawlers_proficiencies)
            rating = calculate_card_rating(quality_vs_enemies)
            status = calculate_card_status_from_rating(rating)

            results[brawler_key] = {
                'index': brawler_key,
                'status': status,
                'rating': rating,
                'quality_vs_enemies': quality_vs_enemies,
            }
            enemy_indexes = get_enemy_indexes(brawler_key)
            for enemy_index in enemy_indexes:
                results[enemy_index]['quality_vs_enemies'][brawler_key] = quality_vs_enemies[enemy_index] * -1

            print("\n\n\n", results, "\n\n\n")
        else:
            results[brawler_key]['index'] = brawler_key
            results[brawler_key]['rating'] = calculate_card_rating(results[brawler_key]['quality_vs_enemies'])
            results[brawler_key]['status'] = calculate_card_status_from_rating(results[brawler_key]['rating'])

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
    print(selected_gadget, card, "eweewewew")

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
        if type(brawler_proficiencies[key]) == str:
            continue
        brawler_proficiencies[key] = value/10
    return brawler_proficiencies

def get_final_brawler_properties(bp):

    weight_object_burst_damage_isr = 1500
    weight_object_burst_damage_imr = 1500
    weight_object_burst_damage_ilr = 1500
    weight_object_burst_damage_ivlr = 1200

    weight_usual_burst_damage_isr = 1300
    weight_usual_burst_damage_imr = 800
    weight_usual_burst_damage_ilr = 400
    weight_usual_burst_damage_ivlr = 250

    # BASIC DAMAGE PROPERTIES
    bp['object_burst_damage_in_short_range'] = round((((bp['_average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_short_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_isr) + ((bp['_pets_damage']*(bp['_pets_range'] / 3)) / 5), 2)
    bp['object_burst_damage_in_medium_range'] = round((((bp['_average_projectiles_per_shot'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_medium_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_imr) + ((bp['_pets_damage']*(bp['_pets_range'] / 5)) / 5), 2)
    bp['object_burst_damage_in_long_range'] = round(((((bp['_average_projectiles_per_shot'] * (bp['_attack_distance'] / 7)) * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_long_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_ilr) + ((bp['_pets_damage']*(bp['_pets_range'] / 7)) / 5), 2)
    bp['object_burst_damage_in_very_long_range'] = round(((((bp['_average_projectiles_per_shot'] * (bp['_attack_distance'] / 9)) * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + bp['super_damage_in_very_long_range'] + (bp['ocasional_damage'] / 4))/weight_object_burst_damage_ivlr) + ((bp['_pets_damage']*(bp['_pets_range'] / 9)) / 5), 2)
    
    bp['usual_burst_damage_in_short_range'] = round((((bp['_projectiles_per_shot_in_short_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['_projectiles_per_shot_in_short_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * bp['super_damage_in_short_range'])) / (1.25 - ((bp['_projectiles_per_shot_in_short_range'] - bp['_average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_isr, 2)
    bp['usual_burst_damage_in_medium_range'] = round((((bp['_projectiles_per_shot_in_medium_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['_projectiles_per_shot_in_medium_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * bp['super_damage_in_medium_range'])) / (1.25 - ((bp['_projectiles_per_shot_in_medium_range'] - bp['_average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_imr, 2)
    bp['usual_burst_damage_in_long_range'] = round((((bp['_projectiles_per_shot_in_long_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['_projectiles_per_shot_in_long_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * bp['super_damage_in_long_range'])) / (1.25 - ((bp['_projectiles_per_shot_in_long_range'] - bp['_average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_ilr, 2)
    bp['usual_burst_damage_in_very_long_range'] = round((((bp['_projectiles_per_shot_in_very_long_range'] * bp['_projectile_damage'] * bp['_shots_per_five_seconds']) + (((bp['_shots_per_five_seconds'] * bp['_projectiles_per_shot_in_very_long_range'] + bp['_auto_charge_super']) / bp['_necessary_projectiles_to_charge_super']) * bp['super_damage_in_very_long_range'])) / (1.25 - ((bp['_projectiles_per_shot_in_very_long_range'] - bp['_average_projectiles_per_shot']) / 4)) + (bp['ocasional_damage'] / 4))/weight_usual_burst_damage_ivlr, 2)

    if bp['usual_burst_damage_in_short_range'] < 0:
        bp['usual_burst_damage_in_short_range'] = 0
    if bp['usual_burst_damage_in_medium_range'] < 0:
        bp['usual_burst_damage_in_medium_range'] = 0
    if bp['usual_burst_damage_in_long_range'] < 0:
        bp['usual_burst_damage_in_long_range'] = 0
    if bp['usual_burst_damage_in_very_long_range'] < 0:
        bp['usual_burst_damage_in_very_long_range'] = 0

    # DAMAGE/DURABILITY RELATIONSHIP PROPERTIES
    bp['balance_between_damage_and_durability_in_short_range'] = round(((bp['usual_burst_damage_in_short_range'] / 2) * (bp['_durability'] / 1)) / 2.5, 2)
    bp['balance_between_damage_and_durability_in_medium_range'] = round(((bp['usual_burst_damage_in_medium_range'] / 1) * (bp['_durability'] / 2)) / 3.5, 2)
    bp['balance_between_damage_and_durability_in_long_range'] = round(((bp['usual_burst_damage_in_long_range'] * 1.5) * (bp['_durability'] / 3)) / 3, 2)
    bp['balance_between_damage_and_durability_in_very_long_range'] = round(((bp['usual_burst_damage_in_very_long_range'] * 2) * (bp['_durability'] / 4)) / 5, 2)

    # SURPRISE ATTACK POWER PROPERTIES
    bp['surprise_attack_power_in_short_range'] = round((bp['_surprise_attack'] * bp['balance_between_damage_and_durability_in_short_range']) / 3, 2)
    bp['surprise_attack_power_in_medium_range'] = round((bp['_surprise_attack'] * bp['balance_between_damage_and_durability_in_medium_range']) / 2.7, 2)
    bp['surprise_attack_power_in_long_range'] = round((bp['_surprise_attack'] * bp['balance_between_damage_and_durability_in_long_range']) / 2.4, 2)
    bp['surprise_attack_power_in_very_long_range'] = round((bp['_surprise_attack'] * bp['balance_between_damage_and_durability_in_very_long_range']) / 1.9, 2)

    # OTHER PROPERTIES
    bp['easy_approach'] = round(((bp['_surprise_attack'] * 4) + (bp['_movement_speed'] * 2) + (bp['_durability'] * 2)) / 6, 2)
    bp['pressure'] = round(((((bp['wide_attack'] + ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range']) / 2) / 1.5) / 2) * 4) + (bp['_durability'] * 4) + (bp['_attack_distance'] * 2) + (bp['easy_approach'] * 2)) / 9, 2)
    bp['area_control'] = round(((bp['area_denial'] * 5) + (((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / (4 * 2)) * 2) + (bp['invisibility_buffing'] * 2)) / 6, 2)

    if bp['_indirect_damage_efficiency'] < 6:
        bp['indirect_damage'] = (bp['_indirect_damage_efficiency'] * bp['average_super_damage']) / 2000
    elif bp['_indirect_damage_efficiency'] < 7:
        bp['indirect_damage'] = bp['_indirect_damage_efficiency'] * ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / (4 * 2.5))
    else:
        bp['indirect_damage'] = bp['_indirect_damage_efficiency'] * ((bp['balance_between_damage_and_durability_in_short_range'] + bp['balance_between_damage_and_durability_in_medium_range'] + bp['balance_between_damage_and_durability_in_long_range'] + bp['balance_between_damage_and_durability_in_very_long_range']) / (4 * 2.5)) * (bp['average_super_damage'] / 2000)
    bp['indirect_damage'] = round(bp['indirect_damage'] / ((10 - bp['_attack_distance'] + 2) / 4), 2)

    bp['multiple_pets_generation'] = round(((bp['_frequency_of_pets_generation'] * 4) + ((bp['_pets_resistence'] * 2) / (bp['_deteriorability_of_pets'] + 1)) + (bp['_accumulation_of_pets'] * 4)) / 7.5, 2)
    bp['durable_pets_generation'] = round(((bp['_pets_resistence'] * 3) + (bp['_frequency_of_pets_generation'] * 3) + ((bp['_pets_damage'] * 2) + (bp['_pets_range'] * 2) + (bp['_pets_speed'] * 2))) / 8, 2)
    bp['groupment_punishment'] = round((((bp['wide_attack'] * 2) + (bp['stun_debuffing'] * 1) + (bp['_increased_damage_when_grouped'] * 3)) / 4.5) * 1.5, 2)

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
            if property_key in ['id', '_necessary_projectiles_to_charge_super', '_necessary_supers_to_charge_hipercharge', '_projectile_damage', '_shots_per_five_seconds', '_average_projectiles_per_shot', '_projectiles_per_shot_in_short_range', '_projectiles_per_shot_in_medium_range', '_projectiles_per_shot_in_long_range', '_projectiles_per_shot_in_very_long_range', '_auto_charge_super', 'super_damage_in_short_range', 'super_damage_in_medium_range', 'super_damage_in_long_range', 'super_damage_in_very_long_range', 'average_super_damage', 'ocasional_damage']:
                continue
            if type(brawlers_proficiencies[brawler_index][property_key]) == str:
                continue
            analized_brawler_power_values = []
            property_relations = PROFICIENCIES_PROPERTIES_RELATIONSHIP[property_key]

            analized_brawler_properties = brawlers_proficiencies[brawler_index]
            analized_enemy_properties = brawlers_proficiencies[enemy_index]

            print("Brawler", brawler_index, ":", property_key, ":", analized_brawler_properties[property_key])

            for weakness in property_relations['weaknesses']:
                weakness_property = weakness[1]
                weakness_weight = weakness[0]
                result1 = (((analized_brawler_properties[property_key] - analized_enemy_properties[weakness_property]) / 10) * analized_brawler_properties[property_key]) * weakness_weight
                result2 = ((((analized_enemy_properties[property_key] - analized_brawler_properties[weakness_property]) / 10) * analized_enemy_properties[property_key]) * weakness_weight) * -1
                result = (result1 + result2) / 2
                analized_brawler_power_values.append(result)
                print("weakness:", weakness_property, analized_enemy_properties[weakness_property], result)

            for useful in property_relations['useful_against']:
                useful_property = useful[1]
                useful_weight = useful[0]
                result1 = ((analized_brawler_properties[property_key] * analized_enemy_properties[useful_property] / 10) / (10 - analized_brawler_properties[property_key])) * useful_weight
                result2 = (((analized_enemy_properties[property_key] * analized_brawler_properties[useful_property] / 10) / (10 - analized_enemy_properties[property_key])) * useful_weight) * -1
                result = (result1 + result2) / 2
                analized_brawler_power_values.append(result)
                print("useful:", useful_property, analized_enemy_properties[useful_property], result)

            result_analized_brawler = 0
            for power in analized_brawler_power_values:
                result_analized_brawler += power
            if len(analized_brawler_power_values) > 0:
                result_analized_brawler /= len(analized_brawler_power_values)
            else:
                result_analized_brawler /= 1

            quality[enemy_index] += result_analized_brawler
    
    good_looking_quality = get_formated_quality(quality)
    return good_looking_quality

def get_formated_quality(quality):
    for enemy_index in quality.keys():
        quality[enemy_index] = round(quality[enemy_index], 2)
    return quality

def get_formated_rating(rating):
    rating = round((rating * 0.5) + 50, 0)
    if rating > 100:
        rating = 100
    elif rating < 0:
        rating = 0
    return rating

def get_enemy_indexes(card_index):
    if card_index in [0, 1, 2]:
        return [3, 4, 5]
    else:
        return [0, 1, 2]

def calculate_card_rating(quality_vs_enemies):
    sum_of_qualities = 0
    for quality in quality_vs_enemies.values():
        sum_of_qualities += quality
    average_quality = sum_of_qualities / 3
    final_average = get_formated_rating(average_quality)
    return final_average

def calculate_card_status_from_rating(rating):
    if rating >= 85:
        return 'Great'
    elif rating >= 70:
        return 'Good'
    elif rating >= 58:
        return 'Oh'
    elif rating > 42:
        return 'Ok'
    elif rating > 30:
        return 'Hmm'
    elif rating > 15:
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