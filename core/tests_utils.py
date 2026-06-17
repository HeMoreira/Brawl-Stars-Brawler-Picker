from proficiency.models import Proficiency
from additional_power.models import Gadget, StarPower, Hipercharge
from brawler.models import Brawler

def _create_additional_power(model, additional_power_name, icon_name):
    return model.objects.create(
        additional_power_name=additional_power_name,
        icon_name=icon_name,
        base_proficiency=Proficiency.objects.create(),
    )

def _create_brawler(name, icon_name, primary_class, secondary_class):
    return Brawler.objects.create(
        name=name,
        icon_name=icon_name,
        primary_class=primary_class,
        secondary_class=secondary_class,
        base_proficiency=Proficiency.objects.create(),
        first_gadget=_create_additional_power(Gadget, name, icon_name),
        second_gadget=_create_additional_power(Gadget, name, icon_name),
        first_starpower=_create_additional_power(StarPower, name, icon_name),
        second_starpower=_create_additional_power(StarPower, name, icon_name),
        hipercharge=_create_additional_power(Hipercharge, name, icon_name),
    )