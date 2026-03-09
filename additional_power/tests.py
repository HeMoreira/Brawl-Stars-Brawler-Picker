from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Gadget, StarPower, Hipercharge
from proficiency.models import Proficiency

# Create your tests here.
class MapModelTest(TestCase):
    def setUp(self):
        self.addpower1 = Gadget(name="Super Test Power", icon_name="supertestpower_icon.png", base_proficiency=Proficiency())
        self.addpower2 = StarPower(name="Test Additional power With many Sp@c3s and stuff", icon_name="testadditionalpowerwithmanysp@c3sandstuff_icon.png", base_proficiency=Proficiency())
        self.addpower3 = Hipercharge(name="OoOneMoreTest", icon_name="ooonemoretest_icon.png", base_proficiency=Proficiency())
    
    def test_acceptable_icon_name_according_to_without_spaces_rule(self):
        self.addpower1.icon_name = "supertestpo-wer_icon.png"
        with self.assertRaises(ValidationError): self.addpower1.clean()
        self.addpower2.icon_name = "t esta-dditional powerwithmanysp@c3sandstuff_icon.png"
        with self.assertRaises(ValidationError): self.addpower2.clean()
        self.addpower3.icon_name = "o-o-onemoretest_icon.png"
        with self.assertRaises(ValidationError): self.addpower3.clean()

    def test_acceptable_icon_name_according_to_correct_end_rule(self):
        self.addpower1.icon_name = "supertestpower_ic0n.png"
        with self.assertRaises(ValidationError): self.addpower1.clean()
        self.addpower2.icon_name = "testadditionalpowerwithmanysp@c3sandstuff_icon.pnG"
        with self.assertRaises(ValidationError): self.addpower2.clean()
        self.addpower3.icon_name = "ooonemoretest_icon.pqg"
        with self.assertRaises(ValidationError): self.addpower3.clean()

    def test_acceptable_icon_name_according_to_exact_name_rule(self):
        self.addpower1.icon_name = "superteetpower_icon.png"
        with self.assertRaises(ValidationError): self.addpower1.clean()
        self.addpower2.icon_name = "testadditionalpowerwithmanysp@cesandstuff_icon.png"
        with self.assertRaises(ValidationError): self.addpower2.clean()
        self.addpower3.icon_name = "oOonemoretest_icon.png"
        with self.assertRaises(ValidationError): self.addpower3.clean()

    def test_acceptable_icon_name(self):
        self.addpower1.icon_name = "supertestpower_icon.png"
        self.addpower2.icon_name = "testadditionalpowerwithmanysp@c3sandstuff_icon.png"
        self.addpower3.icon_name = "ooonemoretest_icon.png"
        try:
            self.addpower1.clean()
            self.addpower2.clean()
            self.addpower3.clean()
        except(ValidationError):
            self.fail("The names should be correct according to the name")