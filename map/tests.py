from django.test import TestCase
from .models import Map
from proficiency.models import Proficiency
from django.core.exceptions import ValidationError

# Create your tests here.
class MapModelTest(TestCase):
    def setUp(self):
        self.map = Map(name="Super Test Map", icon_name="supertestmap_icon.png", mode="GG", proficiency_multiplier=Proficiency())
    
    def test_acceptable_icon_name_according_to_without_spaces_rule(self):
        self.map.icon_name = "super-testmap_icon.png"
        with self.assertRaises(ValidationError): self.map.clean()

    def test_acceptable_icon_name_according_to_correct_end_rule(self):
        self.map.icon_name = "supertestmap_ic0n.png"
        with self.assertRaises(ValidationError): self.map.clean()

    def test_acceptable_icon_name_according_to_exact_name_rule(self):
        self.map.icon_name = "suprrtestmap_icon.png"
        with self.assertRaises(ValidationError): self.map.clean()

    def test_acceptable_icon_name(self):
        self.map.icon_name = "supertestmap_icon.png"
        try:
            self.map.clean()
        except(ValidationError):
            self.fail("The name should be correct according to the name")