from django.test import TestCase
from .models import Proficiency
from django.db import IntegrityError

# Create your tests here.
class ProficiencyModelTest(TestCase):
    


    def test_negative_value_durability_constraint(self):
        proficiency = Proficiency(durability=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_durability_constraint(self):
        proficiency = Proficiency(counter_durability=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_attack_distance_constraint(self):
        proficiency = Proficiency(attack_distance=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_attack_distance_constraint(self):
        proficiency = Proficiency(counter_attack_distance=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_surprise_attack_constraint(self):
        proficiency = Proficiency(surprise_attack=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_surprise_attack_constraint(self):
        proficiency = Proficiency(counter_surprise_attack=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_easy_approximation_constraint(self):
        proficiency = Proficiency(easy_approximation=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_easy_approximation_constraint(self):
        proficiency = Proficiency(counter_easy_approximation=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_burst_damage_constraint(self):
        proficiency = Proficiency(burst_damage=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_burst_damage_constraint(self):
        proficiency = Proficiency(counter_burst_damage=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_objects_burst_damage_constraint(self):
        proficiency = Proficiency(objects_burst_damage=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_objects_burst_damage_constraint(self):
        proficiency = Proficiency(counter_objects_burst_damage=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_indirect_damage_constraint(self):
        proficiency = Proficiency(indirect_damage=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_indirect_damage_constraint(self):
        proficiency = Proficiency(counter_indirect_damage=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_area_denial_constraint(self):
        proficiency = Proficiency(area_denial=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_area_denial_constraint(self):
        proficiency = Proficiency(counter_area_denial=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_multiple_pets_constraint(self):
        proficiency = Proficiency(multiple_pets=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_multiple_pets_constraint(self):
        proficiency = Proficiency(counter_multiple_pets=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_durable_pets_constraint(self):
        proficiency = Proficiency(durable_pets=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_durable_pets_constraint(self):
        proficiency = Proficiency(counter_durable_pets=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_wide_attack_constraint(self):
        proficiency = Proficiency(wide_attack=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_wide_attack_constraint(self):
        proficiency = Proficiency(counter_wide_attack=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_retreat_button_constraint(self):
        proficiency = Proficiency(retreat_button=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_retreat_button_constraint(self):
        proficiency = Proficiency(counter_retreat_button=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_wall_break_efficiency_constraint(self):
        proficiency = Proficiency(wall_break_efficiency=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_wall_break_efficiency_constraint(self):
        proficiency = Proficiency(counter_wall_break_efficiency=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_grass_break_efficiency_constraint(self):
        proficiency = Proficiency(grass_break_efficiency=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_grass_break_efficiency_constraint(self):
        proficiency = Proficiency(counter_grass_break_efficiency=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_enemy_position_manipulation_constraint(self):
        proficiency = Proficiency(enemy_position_manipulation=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_enemy_position_manipulation_constraint(self):
        proficiency = Proficiency(counter_enemy_position_manipulation=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_groupment_punishment_constraint(self):
        proficiency = Proficiency(groupment_punishment=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_groupment_punishment_constraint(self):
        proficiency = Proficiency(counter_groupment_punishment=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_water_walking_constraint(self):
        proficiency = Proficiency(water_walking=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_water_walking_constraint(self):
        proficiency = Proficiency(counter_water_walking=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_heal_buffing_constraint(self):
        proficiency = Proficiency(heal_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_heal_buffing_constraint(self):
        proficiency = Proficiency(counter_heal_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_shield_buffing_constraint(self):
        proficiency = Proficiency(shield_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()
        
    def test_negative_value_counter_shield_buffing_constraint(self):
        proficiency = Proficiency(counter_shield_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_damage_buffing_constraint(self):
        proficiency = Proficiency(damage_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_damage_buffing_constraint(self):
        proficiency = Proficiency(counter_damage_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_speed_buffing_constraint(self):
        proficiency = Proficiency(speed_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_speed_buffing_constraint(self):
        proficiency = Proficiency(counter_speed_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_invisibility_buffing_constraint(self):
        proficiency = Proficiency(invisibility_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_invisibility_buffing_constraint(self):
        proficiency = Proficiency(counter_invisibility_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_positioning_buffing_constraint(self):
        proficiency = Proficiency(positioning_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_positioning_buffing_constraint(self):
        proficiency = Proficiency(counter_positioning_buffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_poison_debuffing_constraint(self):
        proficiency = Proficiency(poison_debuffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_poison_debuffing_constraint(self):
        proficiency = Proficiency(counter_poison_debuffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_stun_debuffing_constraint(self):
        proficiency = Proficiency(stun_debuffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_stun_debuffing_constraint(self):
        proficiency = Proficiency(counter_stun_debuffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_slowness_debuffing_constraint(self):
        proficiency = Proficiency(slowness_debuffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_slowness_debuffing_constraint(self):
        proficiency = Proficiency(counter_slowness_debuffing=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_block_enemies_constraint(self):
        proficiency = Proficiency(block_enemies=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_block_enemies_constraint(self):
        proficiency = Proficiency(counter_block_enemies=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_attacks_canceling_constraint(self):
        proficiency = Proficiency(attacks_canceling=-1)
        with self.assertRaises(IntegrityError): proficiency.save()

    def test_negative_value_counter_attacks_canceling_constraint(self):
        proficiency = Proficiency(counter_attacks_canceling=-1)
        with self.assertRaises(IntegrityError): proficiency.save()