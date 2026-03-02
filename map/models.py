from django.db import models
from proficiency.models import Proficiency

# Create your models here.
class Map(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name of the Map")
    icon_name = models.CharField(max_length=29, verbose_name="Icon of the Map", default="unownmap_icon.png")
    mode = models.CharField(max_length=2, verbose_name="Gamemode of the Map", choices=[('GG', 'Gem-Grab'), ('BW', 'Brawl-Ball'), ('BO', 'Bounty'), ('HE', 'Heist'), ('HZ', 'Hot-Zone'), ('KN', 'Knockout'), ('WO', 'Wipeout'), ('BH', 'Brawl-Hockey'), ('SW', 'Spirit-Wars'), ('PP', 'Present-Plunder'), ('BK', 'Basket-Brawl'), ('VY', 'Volley-Brawl'), ('PT', 'Paint-Brawl'), ('SC', 'Soul-Collector'), ('BA', 'Brawl-Arena'), ('TR', 'Token-Run'), ('TH', 'Treasure-Hunt'), ('DG', 'Dodgebrawl'), ('SB', 'Save-Blast')])
    proficiency_multiplier = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Proficiency Multiplier", help_text="The proficiencies of brawlers and others are multiplied from this map proficiencies, so use 10 by default and rarely use numbers above 25. All numbers here are divided by ten before being used as a multiplier")
