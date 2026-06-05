from django.db import models
from proficiency.models import Proficiency
from django.core.exceptions import ValidationError

class AdditionalPower(models.Model):
    additional_power_name = models.CharField(max_length=40)
    icon_name = models.CharField(max_length=49)
    base_proficiency = models.OneToOneField(Proficiency, on_delete=models.CASCADE, verbose_name="Base Proficiency")

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.additional_power_name
    
    def clean(self):
        super().clean()
        adapted_name = self.additional_power_name.lower().replace(" ", "")
        name_length = len(adapted_name)
        if adapted_name != self.icon_name[:name_length] or self.icon_name[name_length:] != "_icon.png":
            raise ValidationError({'icon_name': 'The icon_name needs to be composed of <brawlernameinlowercaseandwithoutspaces>_icon.png'})
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

class Gadget(AdditionalPower):
    additional_power_name = models.CharField(max_length=40, verbose_name="Gadget Name")
    icon_name = models.CharField(max_length=49,  verbose_name="Gadget Icon Name", default="unowngadget_icon.png")

    class Meta:
        verbose_name = "Gadget"
        verbose_name_plural = "Gadgets"

class StarPower(AdditionalPower):
    additional_power_name = models.CharField(max_length=40, verbose_name="Star Power Name")
    icon_name = models.CharField(max_length=49,  verbose_name="Star Power Icon Name", default="unownstarpower_icon.png")

    class Meta:
        verbose_name = "Star Power"
        verbose_name_plural = "Star Powers"

class Hipercharge(AdditionalPower):
    additional_power_name = models.CharField(max_length=40, verbose_name="Hipercharge Name")
    icon_name = models.CharField(max_length=49,  verbose_name="Hypercharge Icon Name", default="unownhipercharge_icon.png")

    class Meta:
        verbose_name = "Hipercharge"
        verbose_name_plural = "Hipercharges"