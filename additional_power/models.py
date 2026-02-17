from django.db import models
from proficiency.models import Proficiency

# Create your models here.
class Gadget(models.Model):
    name = models.CharField(max_length=40)
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")

    class Meta:
        verbose_name = "Gadget"
        verbose_name_plural = "Gadgets"
    
    def __str__(self):
        return self.name

class StarPower(models.Model):
    name = models.CharField(max_length=40)
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")

    class Meta:
        verbose_name = "Star Power"
        verbose_name_plural = "Star Powers"
    
    def __str__(self):
        return self.name

class Hipercharge(models.Model):
    name = models.CharField(max_length=40)
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")

    class Meta:
        verbose_name = "Hipercharge"
        verbose_name_plural = "Hipercharges"
    
    def __str__(self):
        return self.name