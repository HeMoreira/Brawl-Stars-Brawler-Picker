from django.test import SimpleTestCase
import pandas as pd

from brawler.utils import (
    _get_proficiency_fields,
    _collect_proficiency_values,
    process_single_sheet,
    validate_all_sheets,
)
from proficiency.models import Proficiency

class BrawlerUtilsTest(SimpleTestCase):

    def setUp(self):
        self.durability_field = Proficiency._meta.get_field("_durability")
        self.damage_field = Proficiency._meta.get_field("_projectile_damage")
        self.proficiency_fields = [self.durability_field, self.damage_field]

    def test_get_proficiency_fields_excludes_id_and_includes_known_field(self):
        fields = _get_proficiency_fields()
        field_names = [f.name for f in fields]
        self.assertNotIn("id", field_names)
        self.assertIn("_durability", field_names)
        self.assertIn("_projectile_damage", field_names)

    def test_collect_proficiency_values_returns_scaled_values_without_errors(self):
        row = pd.Series({"_durability": 1.26, "_projectile_damage": 2.04})
        col_by_field = {"_durability": "_durability", "_projectile_damage": "_projectile_damage"}

        values, errors = _collect_proficiency_values(
            row, self.proficiency_fields, col_by_field, "BRAWLERS OFICIAL", "Shelly"
        )

        self.assertEqual(values, {"_durability": 13, "_projectile_damage": 20})
        self.assertEqual(errors, [])

    def test_collect_proficiency_values_reports_error_for_missing_value(self):
        row = pd.Series({"_durability": float("nan"), "_projectile_damage": 2.04})
        col_by_field = {"_durability": "_durability", "_projectile_damage": "_projectile_damage"}

        values, errors = _collect_proficiency_values(
            row, self.proficiency_fields, col_by_field, "BRAWLERS OFICIAL", "Shelly"
        )

        self.assertNotIn("_durability", values)
        self.assertEqual(values["_projectile_damage"], 20)
        self.assertEqual(len(errors), 1)
        self.assertIn("Shelly", errors[0])
        self.assertIn("_durability", errors[0])

    def test_collect_proficiency_values_skips_field_without_mapped_column(self):
        row = pd.Series({"_durability": 1.26})
        # Coluna de _projectile_damage não foi encontrada na validação anterior
        col_by_field = {"_durability": "_durability"}

        values, errors = _collect_proficiency_values(
            row, self.proficiency_fields, col_by_field, "BRAWLERS OFICIAL", "Shelly"
        )

        self.assertEqual(values, {"_durability": 13})
        self.assertEqual(errors, [])

    def test_process_single_sheet_brawlers_oficial_happy_path_and_stop_marker(self):
        df = pd.DataFrame({
            "name": ["Shelly", "Colt", "-"],
            "_durability": [1.26, 1.5, None],
            "_projectile_damage": [2.04, 1.8, None],
        })

        sheet_rows, errors = process_single_sheet("BRAWLERS OFICIAL", df, self.proficiency_fields)

        self.assertEqual(errors, [])
        self.assertEqual(len(sheet_rows), 2)  # parou no "-"
        self.assertEqual(sheet_rows[0]["brawler_name"], "Shelly")
        self.assertEqual(sheet_rows[0]["proficiency_values"], {"_durability": 13, "_projectile_damage": 20})
        self.assertIsNone(sheet_rows[0]["additional_power_name"])

    def test_process_single_sheet_additional_power_collects_power_name(self):
        df = pd.DataFrame({
            "name": ["Shelly"],
            "_durability": [1.26],
            "_projectile_damage": [2.04],
            "additional_power_name": ["Banana"],
        })

        sheet_rows, errors = process_single_sheet("PRIMEIRO ACESSÓRIO", df, self.proficiency_fields)

        self.assertEqual(errors, [])
        self.assertEqual(sheet_rows[0]["additional_power_name"], "Banana")

    def test_process_single_sheet_missing_required_column_aborts_row_collection(self):
        df = pd.DataFrame({
            "name": ["Shelly"],
            "_durability": [1.26],
        })

        sheet_rows, errors = process_single_sheet("BRAWLERS OFICIAL", df, self.proficiency_fields)

        self.assertEqual(sheet_rows, [])
        self.assertEqual(len(errors), 1)
        self.assertIn("_projectile_damage", errors[0])

    def test_process_single_sheet_reports_missing_additional_power_name(self):
        df = pd.DataFrame({
            "name": ["Shelly"],
            "_durability": [1.26],
            "_projectile_damage": [2.04],
            "additional_power_name": [None],
        })

        sheet_rows, errors = process_single_sheet("PRIMEIRO ACESSÓRIO", df, self.proficiency_fields)

        self.assertEqual(len(errors), 1)
        self.assertIn("additional_power_name", errors[0])
        self.assertIn("Shelly", errors[0])

    def test_validate_all_sheets_parses_known_sheets_and_keeps_summary_zeroed(self):
        df_brawlers = pd.DataFrame({
            "idx": [0, 1],
            "name": ["Shelly", "Colt"],
            "_durability": [1.26, 1.5],
            "_projectile_damage": [2.04, 1.8],
        })
        all_sheets = {"BRAWLERS OFICIAL": df_brawlers}

        parsed_sheets, summary = validate_all_sheets(all_sheets, self.proficiency_fields)

        self.assertIn("BRAWLERS OFICIAL", parsed_sheets)
        self.assertEqual(len(parsed_sheets["BRAWLERS OFICIAL"]), 2)
        self.assertEqual(summary["BRAWLERS OFICIAL"], 0)
        self.assertEqual(set(summary.keys()), {
            "BRAWLERS OFICIAL",
            "PRIMEIRO ACESSÓRIO",
            "SEGUNDO ACESSÓRIO",
            "PRIMEIRO PODER-DE-ESTRELA",
            "SEGUNDO PODER-DE-ESTRELA",
            "HIPERCARGA",
        })

    def test_validate_all_sheets_raises_value_error_on_missing_column(self):
        df_brawlers_bad = pd.DataFrame({
            "idx": [0],
            "name": ["Shelly"],
            "_durability": [1.26],
        })
        all_sheets = {"BRAWLERS OFICIAL": df_brawlers_bad}

        with self.assertRaises(ValueError) as ctx:
            validate_all_sheets(all_sheets, self.proficiency_fields)

        self.assertIn("_projectile_damage", str(ctx.exception))
        self.assertIn("IMPORT ABORTED", str(ctx.exception))