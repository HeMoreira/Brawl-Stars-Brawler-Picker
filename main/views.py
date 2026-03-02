from django.shortcuts import render
from brawler.models import Brawler

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def brawler_picker(request):
    brawlers = Brawler.objects.all()
    namelist_of_brawlers_and_icons = []
    for brawler in brawlers:
        namelist_of_brawlers_and_icons.append({"name":brawler.name, "icon":brawler.icon_name})
    context = {
        "brawlers": brawlers,
        "namelist_of_brawlers_and_icons": namelist_of_brawlers_and_icons,
        # "maps":[maps],
    }
    return render(request, 'main/brawler_picker.html', context)

def supporters(request):
    return render(request, 'main/supporters.html')

# def brawler_combinator(request):
#     render(request, 'brawler_combinator.html')