from django.test import TestCase
from .models import Proficiency
from django.db import models

class ProficiencyModelTest(TestCase):
    def setUp(self):
        self.proficiency = Proficiency.objects.create()

    def test_new_proficiency_defaults_every_numeric_field_to_zero(self):
        for field in Proficiency._meta.concrete_fields:
            if field.primary_key:
                continue

            if isinstance(field, (models.IntegerField, models.SmallIntegerField)):
                with self.subTest(field=field.name):
                    self.assertEqual(getattr(self.proficiency, field.name), 0)

    def test_new_proficiency_defaults_every_text_field_to_none(self):
        for field in Proficiency._meta.concrete_fields:
            if field.primary_key:
                continue

            if isinstance(field, models.CharField):
                with self.subTest(field=field.name):
                    self.assertEqual(getattr(self.proficiency, field.name), 'none')
