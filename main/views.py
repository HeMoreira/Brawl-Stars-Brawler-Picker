from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .utils import aggregate_team_proficiencies, analyze_all_cards
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
            'index': int(raw_card.get('index', -1)),
            'name': (raw_card.get('name') or '').strip(),
            'gadget_id': int(raw_card.get('gadget_id', 0)),
            'starpower_id': int(raw_card.get('starpower_id', 0)),
        })

    for card in normalized_cards:
        if card['index'] not in [0, 1, 2, 3, 4, 5]:
            return JsonResponse({"error": "Each card must have a valid index."}, status=400)
    all_cards_results = analyze_all_cards(normalized_cards)
    print(all_cards_results)

    team_proficiencies = {
        'blue': aggregate_team_proficiencies(normalized_cards[:3]),
        'red': aggregate_team_proficiencies(normalized_cards[3:]),
    }
    relative_quality = [
        {
            'index': result['index'],
            'quality_vs_enemies': result['quality_vs_enemies'],
        }
        for result in all_cards_results
    ]

    return JsonResponse({
        'card_results': all_cards_results,
        'team_proficiencies': team_proficiencies,
        'relative_quality': relative_quality,
    })



def supporters(request):
    return render(request, 'main/supporters.html')

# def brawler_combinator(request):
#     render(request, 'brawler_combinator.html')