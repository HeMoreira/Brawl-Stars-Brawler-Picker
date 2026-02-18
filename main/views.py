from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def brawler_picker(request):
    return render(request, 'main/brawler_picker.html')

def supporters(request):
    return render(request, 'main/supporters.html')

# def brawler_combinator(request):
#     render(request, 'brawler_combinator.html')