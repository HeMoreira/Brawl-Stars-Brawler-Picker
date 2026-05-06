from django.shortcuts import render
from brawler.models import Brawler, Gadget, StarPower

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
            "second_star_power": StarPower.objects.get(id=brawler.second_starpower.id).icon_name
            })
    context = {
        "brawlers": brawlers,
        "main_brawler_info_list": main_brawler_info_list,
        # "maps":[maps],
    }
    return render(request, 'main/brawler_picker.html', context)

def supporters(request):
    return render(request, 'main/supporters.html')

# def brawler_combinator(request):
#     render(request, 'brawler_combinator.html')