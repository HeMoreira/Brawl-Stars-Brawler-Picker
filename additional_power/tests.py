# additional_power/tests.py
from django.db import models as dj_models
from django.test import SimpleTestCase, TestCase
from django.core.exceptions import ValidationError

from .models import Gadget, StarPower, Hipercharge
from proficiency.models import Proficiency

class AdditionalPowerModelTest(SimpleTestCase):

    def setUp(self):
        self.addpower1 = Gadget(
            additional_power_name="Super Test Power",
            icon_name="supertestpower_icon.png",
            base_proficiency=Proficiency(),
        )
        self.addpower2 = StarPower(
            additional_power_name="Test Additional power With many Sp@c3s and stuff",
            icon_name="testadditionalpowerwithmanysp@c3sandstuff_icon.png",
            base_proficiency=Proficiency(),
        )
        self.addpower3 = Hipercharge(
            additional_power_name="OoOneMoreTest",
            icon_name="ooonemoretest_icon.png",
            base_proficiency=Proficiency(),
        )

    def test_rejects_icon_name_with_extra_characters_in_name_part(self):
        self.addpower1.icon_name = "supertestpo-wer_icon.png"
        with self.assertRaises(ValidationError):
            self.addpower1.clean()

        self.addpower2.icon_name = "t esta-dditional powerwithmanysp@c3sandstuff_icon.png"
        with self.assertRaises(ValidationError):
            self.addpower2.clean()

        self.addpower3.icon_name = "o-o-onemoretest_icon.png"
        with self.assertRaises(ValidationError):
            self.addpower3.clean()

    def test_rejects_icon_name_with_wrong_suffix(self):
        self.addpower1.icon_name = "supertestpower_ic0n.png"
        with self.assertRaises(ValidationError):
            self.addpower1.clean()

        self.addpower2.icon_name = "testadditionalpowerwithmanysp@c3sandstuff_icon.pnG"
        with self.assertRaises(ValidationError):
            self.addpower2.clean()

        self.addpower3.icon_name = "ooonemoretest_icon.pqg"
        with self.assertRaises(ValidationError):
            self.addpower3.clean()

    def test_rejects_icon_name_that_does_not_match_power_name(self):
        self.addpower1.icon_name = "superteetpower_icon.png"
        with self.assertRaises(ValidationError):
            self.addpower1.clean()

        self.addpower2.icon_name = "testadditionalpowerwithmanysp@cesandstuff_icon.png"
        with self.assertRaises(ValidationError):
            self.addpower2.clean()

        self.addpower3.icon_name = "oOonemoretest_icon.png"
        with self.assertRaises(ValidationError):
            self.addpower3.clean()

    def test_accepts_icon_name_matching_lowercase_name_without_spaces(self):
        self.addpower1.icon_name = "supertestpower_icon.png"
        self.addpower2.icon_name = "testadditionalpowerwithmanysp@c3sandstuff_icon.png"
        self.addpower3.icon_name = "ooonemoretest_icon.png"

        try:
            self.addpower1.clean()
            self.addpower2.clean()
            self.addpower3.clean()
        except ValidationError:
            self.fail("Os icon_names estão corretos e não deveriam levantar ValidationError")


class AdditionalPowerSaveAndStrTest(TestCase):
    """Testa o comportamento de save() e __str__,
    usando instâncias persistidas de Proficiency."""

    def test_save_raises_validation_error_for_inconsistent_icon_name(self):
        gadget = Gadget(
            additional_power_name="Speedy Gadget",
            icon_name="wrong_icon.png",
            base_proficiency=Proficiency.objects.create(),
        )

        with self.assertRaises(ValidationError):
            gadget.save()

        self.assertIsNone(gadget.pk)
        self.assertFalse(Gadget.objects.filter(additional_power_name="Speedy Gadget").exists())

    def test_save_succeeds_with_consistent_icon_name(self):
        gadget = Gadget(
            additional_power_name="Speedy Gadget",
            icon_name="speedygadget_icon.png",
            base_proficiency=Proficiency.objects.create(),
        )

        gadget.save()

        self.assertIsNotNone(gadget.pk)
        saved = Gadget.objects.get(pk=gadget.pk)
        self.assertEqual(saved.additional_power_name, "Speedy Gadget")
        self.assertEqual(saved.icon_name, "speedygadget_icon.png")

    def test_str_returns_additional_power_name(self):
        star_power = StarPower(
            additional_power_name="Shield Generator",
            icon_name="shieldgenerator_icon.png",
            base_proficiency=Proficiency(),
        )
        self.assertEqual(str(star_power), "Shield Generator")