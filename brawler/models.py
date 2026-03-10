from django.db import models
from proficiency.models import Proficiency
from additional_power.models import Gadget, StarPower, Hipercharge
from django.core.exceptions import ValidationError

# Create your models here.
class Brawler(models.Model):
    name = models.CharField(max_length=25, verbose_name="Brawler Name")
    icon_name = models.CharField(max_length=34, verbose_name="Brawler Icon Name", default="unown_icon.png")
    primary_class = models.CharField(max_length=2, choices=[('D', 'Damage Dealer'), ('T', 'Tank'), ('AS', 'Assasin'), ('S', 'Support'), ('C', 'Controler'), ('M', 'Marksman'), ('AT', 'Artillery')], verbose_name="Primary Class")
    secondary_class = models.CharField(max_length=2, choices=[('D', 'Damage Dealer'), ('T', 'Tank'), ('AS', 'Assasin'), ('S', 'Support'), ('C', 'Controler'), ('M', 'Marksman'), ('AT', 'Artillery')], verbose_name="Secondary Class")
    base_proficiency = models.OneToOneField(Proficiency, on_delete=models.CASCADE, verbose_name="Base Proficiency")
    first_gadget = models.OneToOneField(Gadget, on_delete=models.CASCADE, verbose_name="First Gadget", related_name="first_gadget")
    second_gadget = models.OneToOneField(Gadget, on_delete=models.CASCADE, verbose_name="Second Gadget", related_name="second_gadget")
    first_starpower = models.OneToOneField(StarPower, on_delete=models.CASCADE, verbose_name="First Star Power", related_name="first_starpower")
    second_starpower = models.OneToOneField(StarPower, on_delete=models.CASCADE, verbose_name="Second Star Power", related_name="second_starpower")
    hipercharge = models.OneToOneField(Hipercharge, on_delete=models.CASCADE, verbose_name="Hipercharge")
    gadgets = [first_gadget, second_gadget]
    starpowers = [first_starpower, second_starpower]

    class Meta:
        verbose_name = "Brawler"
        verbose_name_plural = "Brawlers"
        ordering = ['primary_class', 'secondary_class']
    
    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        adapted_name = self.name.lower().replace(" ", "")
        name_length = len(adapted_name)
        if adapted_name != self.icon_name[:name_length] or self.icon_name[name_length:] != "_icon.png":
            raise ValidationError({'icon_name': 'The icon_name needs to be composed of <brawlernameinlowercaseandwithoutspaces>_icon.png'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)