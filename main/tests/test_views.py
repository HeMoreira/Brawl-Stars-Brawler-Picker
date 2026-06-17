import json
from unittest.mock import patch

from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from core.tests_utils import _create_brawler
from brawler.models import Brawler


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
 
 
class TestBrawlerPickerPage(TestCase):
    def setUp(self):
        self.response = self.client.get('/match/')
        self.brawler1 = _create_brawler("Incredible Brawler test", "incrediblebrawlertest_icon.png", "AS", "AS")
        self.brawler2 = _create_brawler("AweSome Br@wler test", "awesomebr@wlertest_icon.png", "AS", "AS")
 
    def test_brawler_picker_view_uses_expected_template(self):
        self.assertTemplateUsed(self.response, "main/brawler_picker.html")
 
    def test_brawler_picker_view_returns_correct_status(self):
        self.assertEqual(self.response.status_code, 200)
 
    def test_brawler_picker_context(self):
        response = self.client.get(reverse('brawler_picker'))
        self.assertEqual(len(response.context['brawlers']), 2)
        self.assertEqual(len(response.context['main_brawler_info_list']), 2)
        self.assertContains(response, "Incredible Brawler test")
        self.assertContains(response, "AweSome Br@wler test")
 
    def test_brawler_picker_context_without_brawlers(self):
        Brawler.objects.all().delete()
        response = self.client.get(reverse('brawler_picker'))
        self.assertEqual(len(response.context['brawlers']), 0)
        self.assertEqual(len(response.context['main_brawler_info_list']), 0)
 
    def test_main_brawler_info_list_includes_gadgets_starpowers_and_hipercharge(self):
        response = self.client.get(reverse('brawler_picker'))
        info_list = response.context['main_brawler_info_list']
        info_by_name = {info['name']: info for info in info_list}
 
        brawler1_info = info_by_name['Incredible Brawler test']
 
        self.assertEqual(brawler1_info['icon'], self.brawler1.icon_name)
        self.assertEqual(
            brawler1_info['first_gadget'],
            [self.brawler1.first_gadget.icon_name, self.brawler1.first_gadget.additional_power_name]
        )
        self.assertEqual(
            brawler1_info['second_gadget'],
            [self.brawler1.second_gadget.icon_name, self.brawler1.second_gadget.additional_power_name]
        )
        self.assertEqual(
            brawler1_info['first_star_power'],
            [self.brawler1.first_starpower.icon_name, self.brawler1.first_starpower.additional_power_name]
        )
        self.assertEqual(
            brawler1_info['second_star_power'],
            [self.brawler1.second_starpower.icon_name, self.brawler1.second_starpower.additional_power_name]
        )
        self.assertEqual(
            brawler1_info['hipercharge'],
            [self.brawler1.hipercharge.icon_name, self.brawler1.hipercharge.additional_power_name]
        )
 
 
class TestUpdateCardsView(TestCase):
    def _post(self, payload):
        return self.client.post(
            reverse('update_cards'),
            data=json.dumps(payload),
            content_type='application/json',
        )
 
    def test_update_cards_rejects_get_requests(self):
        response = self.client.get(reverse('update_cards'))
        self.assertEqual(response.status_code, 405)
 
    def test_update_cards_rejects_invalid_json(self):
        response = self.client.post(
            reverse('update_cards'),
            data="not a json payload",
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
 
    def test_update_cards_rejects_card_with_invalid_index(self):
        payload = {'cards': [
            {'index': 6, 'name': 'Some Brawler', 'gadget_id': 0, 'starpower_id': 0}
        ]}
        response = self._post(payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
 
    @patch('main.views.aggregate_team_proficiencies')
    @patch('main.views.analyze_all_cards')
    def test_update_cards_returns_expected_structure_for_valid_payload(self, mock_analyze, mock_aggregate):
        mock_analyze.return_value = [
            {'index': i, 'status': 'Ok', 'rating': 50, 'quality_vs_enemies': {}}
            for i in range(6)
        ]
        mock_aggregate.return_value = {'_durability': 10}
 
        payload = {'cards': [
            {'index': i, 'name': f'Brawler {i}', 'gadget_id': 0, 'starpower_id': 0}
            for i in range(6)
        ]}
        response = self._post(payload)
 
        self.assertEqual(response.status_code, 200)
        data = response.json()
 
        self.assertIn('card_results', data)
        self.assertIn('team_proficiencies', data)
        self.assertIn('relative_quality', data)
 
        self.assertEqual(len(data['card_results']), 6)
        self.assertEqual(len(data['relative_quality']), 6)
        self.assertEqual(data['relative_quality'][0], {'index': 0, 'quality_vs_enemies': {}})
 
        self.assertIn('blue', data['team_proficiencies'])
        self.assertIn('red', data['team_proficiencies'])
        self.assertEqual(data['team_proficiencies']['blue'], {'_durability': 10})
        self.assertEqual(data['team_proficiencies']['red'], {'_durability': 10})
 
        mock_analyze.assert_called_once()
        self.assertEqual(mock_aggregate.call_count, 2)
 
    @patch('main.views.aggregate_team_proficiencies', return_value={})
    @patch('main.views.analyze_all_cards', return_value=[])
    def test_update_cards_normalizes_card_fields(self, mock_analyze, mock_aggregate):
        payload = {'cards': [
            {'index': '0', 'name': '  Spaced Brawler  ', 'gadget_id': '1', 'starpower_id': '2'}
        ]}
        response = self._post(payload)
 
        self.assertEqual(response.status_code, 200)
        normalized_cards = mock_analyze.call_args[0][0]
        self.assertEqual(normalized_cards, [
            {'index': 0, 'name': 'Spaced Brawler', 'gadget_id': 1, 'starpower_id': 2}
        ])
