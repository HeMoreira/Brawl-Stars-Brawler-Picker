from django.test import TestCase, SimpleTestCase
from brawler.models import Brawler
from additional_power.models import Gadget, StarPower, Hipercharge
from proficiency.models import Proficiency
from django.urls import reverse

class TestIndexPage(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_index_view_uses_expected_template(self):
        self.assertTemplateUsed(self.response, "main/index.html")

    def test_index_view_returns_correct_status(self):
        self.assertEqual(self.response.status_code, 200)

class TestSupportersPage(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get('/supporters/')

    def test_credits_view_uses_expected_template(self):
        self.assertTemplateUsed(self.response, "main/supporters.html")

    def test_credits_view_return_correct_status(self):
        self.assertEqual(self.response.status_code, 200)

class TestMatchPage(TestCase):
    def setUp(self):
        self.response = self.client.get('/match/')
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

    def test_brawler_picker_view_uses_expected_template(self):
        self.assertTemplateUsed(self.response, "main/brawler_picker.html")

    def test_brawler_picker_view_returns_correct_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_brawler_picker_context(self):
        response = self.client.get(reverse('brawler_picker'))
        self.assertEqual(len(response.context['brawlers']), 2)
        self.assertEqual(len(response.context['namelist_of_brawlers_and_icons']), 2)
        self.assertContains(response, "Incredible Brawler test")
        self.assertContains(response, "AweSome Br@wler test")

    def test_brawler_picker_context_without_brawlers(self):
        Brawler.objects.all().delete()
        response = self.client.get(reverse('brawler_picker'))
        self.assertEqual(len(response.context['brawlers']), 0)