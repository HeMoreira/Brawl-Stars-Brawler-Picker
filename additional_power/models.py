from django.db import models
from proficiency.models import Proficiency

# Create your models here.
class Gadget(models.Model):
    gadget_id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=40)
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")

class StarPower(models.Model):
    starpower_id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=40)
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")

class Hipercharge(models.Model):
    hipercharge_id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=40)
    base_proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, verbose_name="Base Proficiency")