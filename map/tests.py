from django.test import TestCase
from .models import Map
from proficiency.models import Proficiency
from django.core.exceptions import ValidationError

# Create your tests here.
class MapModelTest(TestCase):
    def setUp(self):
        self.map1 = Map(name="Super Test Map", icon_name="supertestmap_icon.png", mode="GG", proficiency_multiplier=Proficiency())
        self.map2 = Map(name="Test Map With many Sp@c3s and stuff", icon_name="testmapwithmanysp@c3sandstuff_icon.png", mode="BB", proficiency_multiplier=Proficiency())
    
    def test_acceptable_icon_name_according_to_without_spaces_rule(self):
        self.map1.icon_name = "super-testmap_icon.png"
        with self.assertRaises(ValidationError): self.map1.clean()
        self.map2.icon_name = "testmap-withmany sp@c3sandstuff_icon.png"
        with self.assertRaises(ValidationError): self.map2.clean()

    def test_acceptable_icon_name_according_to_correct_end_rule(self):
        self.map1.icon_name = "supertestmap_ic0n.png"
        with self.assertRaises(ValidationError): self.map1.clean()
        self.map2.icon_name = "testmapwithmanysp@c3sandstuff_iconn.png"
        with self.assertRaises(ValidationError): self.map2.clean()

    def test_acceptable_icon_name_according_to_exact_name_rule(self):
        self.map1.icon_name = "suprrtestmap_icon.png"
        with self.assertRaises(ValidationError): self.map1.clean()
        self.map2.icon_name = "testmapwithmanyspac3sandstuff_icon.png"
        with self.assertRaises(ValidationError): self.map2.clean()

    def test_acceptable_icon_name(self):
        self.map1.icon_name = "supertestmap_icon.png"
        self.map2.icon_name = "testmapwithmanysp@c3sandstuff_icon.png"
        try:
            self.map1.clean()
            self.map2.clean()
        except(ValidationError):
            self.fail("The names should be correct according to the name")