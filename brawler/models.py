from django.db import models
from proficiency.models import Proficiency

# Create your models here.
class Brawler(models.Model):
    name = models.CharField(max_length=25, verbose_name="Brawler Name")
    primary_class = models.CharField(max_length=2, choices=[('D', 'Damage Dealer'), ('T', 'Tank'), ('AS', 'Assasin'), ('S', 'Support'), ('C', 'Controler'), ('M', 'Marksman'), ('AT', 'Artillery')], verbose_name="Primary Class")
    secondary_class = models.CharField(max_length=2, choices=[('D', 'Damage Dealer'), ('T', 'Tank'), ('AS', 'Assasin'), ('S', 'Support'), ('C', 'Controler'), ('M', 'Marksman'), ('AT', 'Artillery')], verbose_name="Secondary Class")
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")
    # first_gadget
    # second_gadget
    # first_star_power
    # second_star_power
    # hipercharge

    class Meta:
        verbose_name = "Brawler"
        verbose_name_plural = "Brawlers"
        ordering = ['primary_class', 'secondary_class']
    
    def __str__(self):
        return self.name