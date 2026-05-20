from brawler.models import Brawler
# from additional_power.models import Gadget, StarPower
from django.db import models


def analyze_all_cards(all_cards):
    results = []
    brawlers_proficiencies = {
        0 : {},
        1 : {},
        2 : {},
        3 : {},
        4 : {},
        5 : {},
    }
    for card in all_cards:
        brawler = find_brawler(card['name'])
        if not brawler:
            brawlers_proficiencies[card['index']] = {}
            continue
        
        # Somar as proficiências de cada brawler com as de seus gadgets, star powers e hipercharges
        # Passar apenas essas informações para brawler_proficiencies, para depois comparar as proficiências de cada brawler com as dos inimigos
    
    for brawler_key, brawler_proficiency_value in brawlers_proficiencies.items():
        ...
        # Comparar as proficiências de cada brawler com as de cada um dos seus inimigos, para obter a nova qualidade de cada brawler contra cada inimigo =@=
        # Calcular a nota do brawler com base nessas qualidades =@=
        # Calcular o status do brawler com base na nota =@=
        # Adicionar a informação à variavel results, que será retornada no final da função =@=

        quality_vs_enemies = calculate_quality_vs_enemies(all_cards[brawler_key], brawlers_proficiencies)
        rating = calculate_card_rating(quality_vs_enemies)
        status = calculate_card_status_from_rating(rating)

        if find_brawler(all_cards[brawler_key]['name']):
            results.append({
                'index': brawler_key,
                'status': status,
                'rating': rating,
                'quality_vs_enemies': quality_vs_enemies,
            })
        else:
            results.append(return_invalid_brawler(brawler_key))

    return results

def find_brawler(name):
    if not name:
        return None
    return Brawler.objects.filter(name__iexact=name.strip()).first()

def return_invalid_brawler(index=None):
    return {
        'index': index,
        'status': 'Invalid',
        'rating': 0,
        'quality_vs_enemies': {},
    }

def calculate_quality_vs_enemies(brawler_index, brawlers_proficiencies):
    enemy_indexes = get_enemy_indexes(brawler_index)
    quality = {}
    for enemy_index in enemy_indexes:
        ...
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