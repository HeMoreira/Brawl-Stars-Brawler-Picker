from django.test import TestCase
from .models import Proficiency

class ProficiencyModelTest(TestCase):
    def test_new_proficiency_defaults_every_numeric_field_to_zero(self):
        proficiency = Proficiency.objects.create()

        for field in Proficiency._meta.concrete_fields:
            if field.primary_key:
                continue

            with self.subTest(field=field.name):
                self.assertEqual(getattr(proficiency, field.name), 0)
