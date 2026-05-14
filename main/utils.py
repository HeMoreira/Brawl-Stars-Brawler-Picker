from brawler.models import Brawler
# from additional_power.models import Gadget, StarPower
from django.db import models


def analyze_card(card, all_cards):
    brawler = find_brawler(card['name'])
    if not brawler:
        return return_invalid_brawler(card['index'])

    quality_vs_enemies = calculate_quality_vs_enemies(card, all_cards)
    rating = calculate_card_rating(quality_vs_enemies)
    status = calculate_card_status_from_rating(rating)

    return {
        'index': card['index'],
        'status': status,
        'rating': rating,
        'quality_vs_enemies': quality_vs_enemies,
    }

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

def calculate_quality_vs_enemies(card, all_cards):
    enemy_indexes = get_enemy_indexes(card['index'])
    quality = {}
    for enemy_index in enemy_indexes:
        quality[enemy_index] = "X"
        ...
        
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