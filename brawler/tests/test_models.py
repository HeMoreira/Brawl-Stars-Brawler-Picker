from django.core.exceptions import ValidationError
from django.test import TestCase

from additional_power.models import Gadget, Hipercharge, StarPower
from brawler.models import Brawler
from proficiency.models import Proficiency

from core.tests_utils import _create_brawler

class BrawlerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.brawler1 = _create_brawler(
            name="Incredible Brawler test",
            icon_name="incrediblebrawlertest_icon.png",
            primary_class="T",
            secondary_class="AS",
        )
        cls.brawler2 = _create_brawler(
            name="AweSome Br@wler test",
            icon_name="awesomebr@wlertest_icon.png",
            primary_class="AT",
            secondary_class="S",
        )

    def test_string_representation_returns_name(self):
        self.assertEqual(str(self.brawler1), "Incredible Brawler test")

    def test_clean_rejects_icon_names_that_do_not_match_the_brawler_name(self):
        invalid_icon_names = [
            "incredible brawler test_icon.png",
            "incrediblebrawlertest_iCOn.png",
            "incrediblibrawlerteet_icon.png",
        ]

        for icon_name in invalid_icon_names:
            with self.subTest(icon_name=icon_name):
                self.brawler1.icon_name = icon_name
                with self.assertRaises(ValidationError):
                    self.brawler1.clean()

    def test_clean_accepts_valid_icon_names(self):
        valid_cases = [
            (self.brawler1, "incrediblebrawlertest_icon.png"),
            (self.brawler2, "awesomebr@wlertest_icon.png"),
        ]

        for brawler, icon_name in valid_cases:
            with self.subTest(brawler=brawler.name):
                brawler.icon_name = icon_name
                brawler.clean()

    def test_save_rejects_invalid_icon_name(self):
        self.brawler1.icon_name = "incredible brawler test_icon.png"

        with self.assertRaises(ValidationError):
            self.brawler1.save()
