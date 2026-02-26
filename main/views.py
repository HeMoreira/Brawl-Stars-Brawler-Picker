from django.shortcuts import render
from brawler.models import Brawler

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def brawler_picker(request):
    context = {
        "brawlers": Brawler.objects.all(),
        # "maps":[maps],
    }
    return render(request, 'main/brawler_picker.html', context)

def supporters(request):
    return render(request, 'main/supporters.html')

# def brawler_combinator(request):
#     render(request, 'brawler_combinator.html')