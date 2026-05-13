from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import models
import json

from brawler.models import Brawler, Gadget, StarPower, Hipercharge

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def brawler_picker(request):
    brawlers = Brawler.objects.all()
    main_brawler_info_list = []
    for brawler in brawlers:
        main_brawler_info_list.append({
            "name": brawler.name,
            "icon": brawler.icon_name,
            "first_gadget": Gadget.objects.get(id=brawler.first_gadget.id).icon_name,
            "second_gadget": Gadget.objects.get(id=brawler.second_gadget.id).icon_name,
            "first_star_power": StarPower.objects.get(id=brawler.first_starpower.id).icon_name,
            "second_star_power": StarPower.objects.get(id=brawler.second_starpower.id).icon_name,
            "hipercharge": Hipercharge.objects.get(id=brawler.hipercharge.id).icon_name,
        })
    context = {
        "brawlers": brawlers,
        "main_brawler_info_list": main_brawler_info_list,
        # "maps":[maps],
    }
    return render(request, 'main/brawler_picker.html', context)

@require_http_methods(["POST"])
def update_card(request):
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    cards = payload.get('cards', [])
    normalized_cards = []

    for raw_card in cards:
        normalized_cards.append({
            'index': int(raw_card.get('index', 0)),
            'name': (raw_card.get('name') or '').strip(),
            'gadget_id': int(raw_card.get('gadget_id', 0) or 0),
            'starpower_id': int(raw_card.get('starpower_id', 0) or 0),
        })

    card_results = [analyze_card(card, normalized_cards) for card in normalized_cards]
    team_proficiencies = {
        'blue': aggregate_team_proficiencies(normalized_cards[:3]),
        'red': aggregate_team_proficiencies(normalized_cards[3:]),
    }
    relative_quality = [
        {
            'index': result['index'],
            'quality_vs_enemies': result['quality_vs_enemies'],
        }
        for result in card_results
    ]

    return JsonResponse({
        'card_results': card_results,
        'team_proficiencies': team_proficiencies,
        'relative_quality': relative_quality,
    })


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

def supporters(request):
    return render(request, 'main/supporters.html')

# def brawler_combinator(request):
#     render(request, 'brawler_combinator.html')