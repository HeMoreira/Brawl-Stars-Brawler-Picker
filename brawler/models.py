from django.db import models
from proficiency.models import Proficiency
from additional_power.models import Gadget, StarPower, Hipercharge

# Create your models here.
class Brawler(models.Model):
    name = models.CharField(max_length=25, verbose_name="Brawler Name")
    primary_class = models.CharField(max_length=2, choices=[('D', 'Damage Dealer'), ('T', 'Tank'), ('AS', 'Assasin'), ('S', 'Support'), ('C', 'Controler'), ('M', 'Marksman'), ('AT', 'Artillery')], verbose_name="Primary Class")
    secondary_class = models.CharField(max_length=2, choices=[('D', 'Damage Dealer'), ('T', 'Tank'), ('AS', 'Assasin'), ('S', 'Support'), ('C', 'Controler'), ('M', 'Marksman'), ('AT', 'Artillery')], verbose_name="Secondary Class")
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")
    first_gadget = models.ForeignKey(Gadget, on_delete=models.PROTECT, verbose_name="First Gadget", related_name="first_gadget")
    second_gadget = models.ForeignKey(Gadget, on_delete=models.PROTECT, verbose_name="Second Gadget", related_name="second_gadget")
    first_starpower = models.ForeignKey(StarPower, on_delete=models.PROTECT, verbose_name="First Star Power", related_name="first_starpower")
    second_starpower = models.ForeignKey(StarPower, on_delete=models.PROTECT, verbose_name="Second Star Power", related_name="second_starpower")
    gadgets = [first_gadget, second_gadget]
    starpowers = [first_starpower, second_starpower]
    hipercharge = models.ForeignKey(Hipercharge, on_delete=models.PROTECT, verbose_name="Hipercharge")

    class Meta:
        verbose_name = "Brawler"
        verbose_name_plural = "Brawlers"
        ordering = ['primary_class', 'secondary_class']
    
    def __str__(self):
        return self.name