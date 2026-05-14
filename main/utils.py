from brawler.models import Brawler
from additional_power.models import Gadget
from django.db import models


def find_brawler(name):
    if not name:
        return None
    return Brawler.objects.filter(name__iexact=name.strip()).first()


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


def aggregate_team_proficiencies(cards):
    totals = {}
    for card in cards:
        brawler = find_brawler(card['name'])
        if not brawler:
            continue
        merge_proficiency_dicts(totals, get_proficiency_values(brawler.base_proficiency))
    return totals


def calculate_card_rating(brawler, gadget, starpower):
    if not brawler:
        return 0

    proficiency = get_proficiency_values(brawler.base_proficiency)
    base_score = sum(proficiency.values()) / 25.0

    if gadget and (brawler.first_gadget == gadget or brawler.second_gadget == gadget):
        base_score += 15
    if starpower and (brawler.first_starpower == starpower or brawler.second_starpower == starpower):
        base_score += 15

    return max(0, min(100, int(base_score)))


def card_status_from_rating(rating):
    if rating >= 80:
        return 'Great'
    if rating >= 60:
        return 'Good'
    if rating >= 40:
        return 'Ok'
    if rating >= 20:
        return 'Bad'
    return 'Awful'


def analyze_card(card, all_cards):
    brawler = find_brawler(card['name'])
    gadget = Gadget.objects.filter(id=card['gadget_id']).first() if card['gadget_id'] else None
    starpower = StarPower.objects.filter(id=card['starpower_id']).first() if card['starpower_id'] else None

    if not brawler:
        return {
            'index': card['index'],
            'status': 'Invalid',
            'rating': 0,
            'quality_vs_enemies': {},
        }

    rating = calculate_card_rating(brawler, gadget, starpower)
    status = card_status_from_rating(rating)
    quality_vs_enemies = calculate_quality_vs_enemies(card, all_cards)

    return {
        'index': card['index'],
        'status': status,
        'rating': rating,
        'quality_vs_enemies': quality_vs_enemies,
    }


def calculate_quality_vs_enemies(card, all_cards):
    own_brawler = find_brawler(card['name'])
    if not own_brawler:
        return {}

    own_rating = calculate_card_rating(
        own_brawler,
        Gadget.objects.filter(id=card['gadget_id']).first() if card['gadget_id'] else None,
        StarPower.objects.filter(id=card['starpower_id']).first() if card['starpower_id'] else None,
    )

    opponent_indexes = [3, 4, 5] if card['index'] < 3 else [0, 1, 2]
    quality = {}

    for opponent_index in opponent_indexes:
        opponent_card = next((item for item in all_cards if item['index'] == opponent_index), None)
        if not opponent_card:
            continue

        opponent_brawler = find_brawler(opponent_card['name'])
        if not opponent_brawler:
            quality[str(opponent_index)] = 0
            continue

        opponent_rating = calculate_card_rating(
            opponent_brawler,
            Gadget.objects.filter(id=opponent_card['gadget_id']).first() if opponent_card['gadget_id'] else None,
            StarPower.objects.filter(id=opponent_card['starpower_id']).first() if opponent_card['starpower_id'] else None,
        )
        quality_value = 50 + (own_rating - opponent_rating)
        quality[str(opponent_index)] = max(0, min(100, quality_value))

    return quality