from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Brawler
from proficiency.models import Proficiency
from additional_power.models import Gadget, StarPower, Hipercharge

# Create your tests here.
class BrawlModelTest(TestCase):
    def setUp(self):
        self.brawler1_data = {
            'name': 'Incredible Brawler test',
            'icon_name': 'incrediblebrawlertest_icon.png',
            'primary_class': 'T',
            'secondary_class': 'AS',
            'base_proficiency': Proficiency.objects.create(),
            'first_gadget': Gadget.objects.create(name="Randim Gadget", icon_name="randimgadget_icon.png", base_proficiency=Proficiency.objects.create()),
            'second_gadget': Gadget.objects.create(name="Random Gadget", icon_name="randomgadget_icon.png", base_proficiency=Proficiency.objects.create()),
            'first_starpower': StarPower.objects.create(name="Randim Star Power", icon_name="randimstarpower_icon.png", base_proficiency=Proficiency.objects.create()),
            'second_starpower': StarPower.objects.create(name="Random Star Power", icon_name="randomstarpower_icon.png", base_proficiency=Proficiency.objects.create()),
            'hipercharge': Hipercharge.objects.create(name="Randim Hipercharge", icon_name="randimhipercharge_icon.png", base_proficiency=Proficiency.objects.create()),
        }
        self.brawler2_data = {
            'name': 'AweSome Br@wler test',
            'icon_name': 'awesomebr@wlertest_icon.png',
            'primary_class': 'AT',
            'secondary_class': 'S',
            'base_proficiency': Proficiency.objects.create(),
            'first_gadget': Gadget.objects.create(name="Randam Gadget", icon_name="randamgadget_icon.png", base_proficiency=Proficiency.objects.create()),
            'second_gadget': Gadget.objects.create(name="Randum Gadget", icon_name="randumgadget_icon.png", base_proficiency=Proficiency.objects.create()),
            'first_starpower': StarPower.objects.create(name="Randam Star Power", icon_name="randamstarpower_icon.png", base_proficiency=Proficiency.objects.create()),
            'second_starpower': StarPower.objects.create(name="Randum Star Power", icon_name="randumstarpower_icon.png", base_proficiency=Proficiency.objects.create()),
            'hipercharge': Hipercharge.objects.create(name="Randem Hipercharge", icon_name="randemhipercharge_icon.png", base_proficiency=Proficiency.objects.create()),
        }
        self.brawler1 = Brawler.objects.create(**self.brawler1_data)
        self.brawler2 = Brawler.objects.create(**self.brawler2_data)
    
    def test_acceptable_icon_name_according_to_without_spaces_rule(self):
        self.brawler1.icon_name = "incredible brawler test_icon.png"
        with self.assertRaises(ValidationError): self.brawler1.clean()
        self.brawler2.icon_name = "awesome- -br@wlertest_icon.png"
        with self.assertRaises(ValidationError): self.brawler2.clean()

    def test_acceptable_icon_name_according_to_correct_end_rule(self):
        self.brawler1.icon_name = "incrediblebrawlertest_iCOn.png"
        with self.assertRaises(ValidationError): self.brawler1.clean()
        self.brawler2.icon_name = "awesomebr@wlertest_icon,png"
        with self.assertRaises(ValidationError): self.brawler2.clean()

    def test_acceptable_icon_name_according_to_exact_name_rule(self):
        self.brawler1.icon_name = "incrediblibrawlerteet_icon.png"
        with self.assertRaises(ValidationError): self.brawler1.clean()
        self.brawler2.icon_name = "awesonebr@wlertest_icon.png"
        with self.assertRaises(ValidationError): self.brawler2.clean()

    def test_acceptable_icon_name(self):
        self.brawler1.icon_name = "incrediblebrawlertest_icon.png"
        self.brawler2.icon_name = "awesomebr@wlertest_icon.png"
        try:
            self.brawler1.clean()
            self.brawler2.clean()
        except(ValidationError):
            self.fail("The names should be correct according to the name")