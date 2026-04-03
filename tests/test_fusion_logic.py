import os
import sys
import unittest

# Adjust path to import from app/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from fusion_logic import TriageFusionEngine

class TestTriageFusionEngine(unittest.TestCase):
    
    def setUp(self):
        self.engine = TriageFusionEngine()

    def test_high_priority_damage_case(self):
        # damaged + very negative -> P1
        vis_data = {"damage_severity": 5}
        text_data = {"sentiment_severity": 5}
        
        result = self.engine.calculate_priority_score(vis_data, text_data)
        
        self.assertAlmostEqual(result["priority_score"], 4.0)
        self.assertEqual(result["route"], "P1_ESCALATION")

    def test_medium_priority_damage_case(self):
        # damaged + neutral -> P2
        vis_data = {"damage_severity": 4} # 4 * 0.5 = 2.0
        text_data = {"sentiment_severity": 2} # 2 * 0.3 = 0.6
        # claim_match = 0
        # total = 2.6 -> P2
        
        result = self.engine.calculate_priority_score(vis_data, text_data)
        
        self.assertTrue(2.5 <= result["priority_score"] < 4.0)
        self.assertEqual(result["route"], "P2_ESCALATION")
        
    def test_low_priority_no_damage(self):
        # no damage + negative text only -> routine/manual review
        vis_data = {"damage_severity": 0} # 0 * 0.5 = 0
        text_data = {"sentiment_severity": 3} # 3 * 0.3 = 0.9
        # claim_match = 3 (since damage=0, sentiment=3) -> 3 * 0.2 = 0.6
        # total = 1.5 -> Routine queue

        result = self.engine.calculate_priority_score(vis_data, text_data)
        
        self.assertTrue(result["priority_score"] < 2.5)
        self.assertEqual(result["route"], "NORMAL_QUEUE")

if __name__ == '__main__':
    unittest.main()
