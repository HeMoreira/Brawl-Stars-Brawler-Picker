from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('match/', views.brawler_picker, name="brawler_picker"),
    path('match/api/update-card/', views.update_card, name="update_card"),
    path('supporters/', views.supporters, name="supporters"),
]