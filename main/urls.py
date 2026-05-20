from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('match/', views.brawler_picker, name="brawler_picker"),
    path('match/api/update-cards/', views.update_cards, name="update_cards"),
    path('supporters/', views.supporters, name="supporters"),
]