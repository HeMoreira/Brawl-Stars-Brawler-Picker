from django.test import TestCase, SimpleTestCase

from core.tests_utils import _create_brawler
from proficiency.models import Proficiency

from main.utils import (
    find_brawler,
    find_gadget,
    find_starpower,
    get_brawler_proficiency,
    get_brawler_total_proficiency,
    convert_proficiencies,
    get_final_brawler_properties,
    get_enemy_indexes,
    calculate_card_rating,
    get_formated_rating,
    calculate_card_status_from_rating,
    return_invalid_brawler,
    calculate_quality_vs_enemies,
    analyze_all_cards
)

class TestBrawlerLookupHelpers(TestCase):
    def setUp(self):
        self.brawler = _create_brawler("Lookup Brawler", "lookupbrawler_icon.png", "T", "AS")
 
    def test_find_brawler_is_case_and_space_insensitive(self):
        self.assertEqual(find_brawler("  lookup brawler  "), self.brawler)
 
    def test_find_brawler_returns_none_for_unknown_or_empty_name(self):
        self.assertIsNone(find_brawler("Does Not Exist"))
        self.assertIsNone(find_brawler(""))
        self.assertIsNone(find_brawler(None))
 
    def test_find_gadget_returns_correct_gadget_by_index(self):
        self.assertEqual(find_gadget("Lookup Brawler", 1), self.brawler.first_gadget)
        self.assertEqual(find_gadget("Lookup Brawler", 2), self.brawler.second_gadget)
        self.assertIsNone(find_gadget("Lookup Brawler", 0))
 
    def test_find_starpower_returns_correct_starpower_by_index(self):
        self.assertEqual(find_starpower("Lookup Brawler", 1), self.brawler.first_starpower)
        self.assertEqual(find_starpower("Lookup Brawler", 2), self.brawler.second_starpower)
        self.assertIsNone(find_starpower("Lookup Brawler", 3))
 
 
class TestBrawlerProficiencyBuilding(TestCase):
 
    def setUp(self):
        self.brawler = _create_brawler("Proficiency Brawler", "proficiencybrawler_icon.png", "T", "AS")
        self.brawler.base_proficiency = Proficiency.objects.create(_projectile_damage=10)
        self.brawler.first_gadget.base_proficiency = Proficiency.objects.create(_projectile_damage=5)
        self.brawler.first_starpower.base_proficiency = Proficiency.objects.create(_projectile_damage=3)

    def test_get_brawler_total_proficiency_ignores_unselected_gadget_and_starpower(self):
        card = {'name': 'Proficiency Brawler', 'gadget_id': 0, 'starpower_id': 0}
        total = get_brawler_total_proficiency(self.brawler, card)
        self.assertEqual(total['_projectile_damage'], 10)
 
    def test_get_brawler_proficiency_returns_empty_dict_for_unknown_brawler(self):
        card = {'name': 'Unknown Brawler', 'gadget_id': 0, 'starpower_id': 0}
        self.assertEqual(get_brawler_proficiency(card), {})
 
    def test_convert_proficiencies_divides_all_values_by_ten(self):
        proficiencies = {'_projectile_damage': 20, '_durability': 5}
        converted = convert_proficiencies(proficiencies)
        self.assertEqual(converted['_projectile_damage'], 2.0)
        self.assertEqual(converted['_durability'], 0.5)
 
 
class TestGetFinalBrawlerProperties(SimpleTestCase):
    def setUp(self):
        self.base_proficiencies = {
            '_average_projectiles_per_shot': 0,
            '_projectile_damage': 0,
            '_shots_per_five_seconds': 0,
            '_pets_damage': 0,
            '_pets_range': 0,
            '_attack_distance': 0,
            '_projectiles_per_shot_in_short_range': 0,
            '_projectiles_per_shot_in_medium_range': 0,
            '_projectiles_per_shot_in_long_range': 0,
            '_projectiles_per_shot_in_very_long_range': 0,
            '_auto_charge_super': 0,
            '_necessary_projectiles_to_charge_super': 1,
            '_durability': 10,
            '_surprise_attack': 5,
            '_movement_speed': 4,
            '_indirect_damage_efficiency': 0,
            '_frequency_of_pets_generation': 0,
            '_pets_resistence': 0,
            '_deteriorability_of_pets': 0,
            '_accumulation_of_pets': 0,
            '_pets_speed': 0,
            '_increased_damage_when_grouped': 0,
            'super_damage_in_short_range': 0,
            'super_damage_in_medium_range': 0,
            'super_damage_in_long_range': 0,
            'super_damage_in_very_long_range': 0,
            'ocasional_damage': 0,
            'wide_attack': 0,
            'area_denial': 0,
            'invisibility_buffing': 0,
            'average_super_damage': 0,
            'stun_debuffing': 0,
        }
 
    def test_removes_private_fields_and_computes_known_properties(self):
        result = get_final_brawler_properties(self.base_proficiencies)
 
        for key in result.keys():
            self.assertFalse(key.startswith('_'), f"Chave privada '{key}' não foi removida")
 
        # easy_approach = ((_surprise_attack*4) + (_movement_speed*2) + (_durability*2)) / 6
        # = ((5*4) + (4*2) + (10*2)) / 6 = 48 / 6 = 8.0
        self.assertEqual(result['easy_approach'], 8.0)
 
        # pressure depende de easy_approach e dos balances (zerados aqui)
        # = ((((0/2)/1.5)*4) + (10*4) + (0*2) + (8.0*2)) / 9 ~= 6.22
        self.assertEqual(result['pressure'], 6.22)
 
        # Sem nenhum dano configurado, os bursts de dano devem ser zero
        self.assertEqual(result['object_burst_damage_in_short_range'], 0)
        self.assertEqual(result['usual_burst_damage_in_short_range'], 0)
        self.assertEqual(result['indirect_damage'], 0)
 
 
class TestCardRatingHelpers(SimpleTestCase):
    def test_get_enemy_indexes_returns_opposite_team(self):
        self.assertEqual(get_enemy_indexes(0), [3, 4, 5])
        self.assertEqual(get_enemy_indexes(1), [3, 4, 5])
        self.assertEqual(get_enemy_indexes(2), [3, 4, 5])
        self.assertEqual(get_enemy_indexes(3), [0, 1, 2])
        self.assertEqual(get_enemy_indexes(4), [0, 1, 2])
        self.assertEqual(get_enemy_indexes(5), [0, 1, 2])
 
    def test_calculate_card_rating_pipeline_for_decent_card(self):
        quality_vs_enemies = {3: 20, 4: 20, 5: 20}
        rating = calculate_card_rating(quality_vs_enemies)
        # average_quality = 20 -> (20*0.5)+50 = 60
        self.assertEqual(rating, 60)
        self.assertEqual(calculate_card_status_from_rating(rating), 'Oh')
 
    def test_calculate_card_rating_pipeline_clamps_to_hundred(self):
        quality_vs_enemies = {0: 100, 1: 100, 2: 100}
        rating = calculate_card_rating(quality_vs_enemies)
        # average_quality = 100 -> (100*0.5)+50 = 100 (limite máximo)
        self.assertEqual(rating, 100)
        self.assertEqual(calculate_card_status_from_rating(rating), 'Great')
 
    def test_get_formated_rating_clamps_between_zero_and_hundred(self):
        self.assertEqual(get_formated_rating(200), 100)
        self.assertEqual(get_formated_rating(-200), 0)
        self.assertEqual(get_formated_rating(0), 50)
 
    def test_calculate_card_status_from_rating_thresholds(self):
        self.assertEqual(calculate_card_status_from_rating(85), 'Great')
        self.assertEqual(calculate_card_status_from_rating(70), 'Good')
        self.assertEqual(calculate_card_status_from_rating(58), 'Oh')
        self.assertEqual(calculate_card_status_from_rating(43), 'Ok')
        self.assertEqual(calculate_card_status_from_rating(31), 'Hmm')
        self.assertEqual(calculate_card_status_from_rating(16), 'Bad')
        self.assertEqual(calculate_card_status_from_rating(10), 'Awful')
 
    def test_return_invalid_brawler_structure(self):
        result = return_invalid_brawler(2)
        self.assertEqual(result, {
            'index': 2,
            'status': 'Invalid',
            'rating': 0,
            'quality_vs_enemies': {},
        })