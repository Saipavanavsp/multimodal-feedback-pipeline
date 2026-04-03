import os
import sys
import unittest

# Adjust path to import from app/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from fusion_logic import TriageFusionEngine

class TestTriageFusionEngine(unittest.TestCase):
    
    def setUp(self):
        self.engine = TriageFusionEngine()

    def test_claim_alignment_high(self):
        # 0 damage but extremely angry
        risk = self.engine.assess_claim_alignment(damage_severity=0, sentiment_severity=5)
        self.assertEqual(risk, 5)

    def test_claim_alignment_low(self):
        # High damage, high anger - makes sense, low risk of mismatch
        risk = self.engine.assess_claim_alignment(damage_severity=4, sentiment_severity=5)
        self.assertEqual(risk, 0)
        
    def test_priority_score_p1_alert(self):
        vis_data = {"damage_severity": 5}
        text_data = {"sentiment_severity": 5}
        
        result = self.engine.calculate_priority_score(vis_data, text_data)
        
        self.assertAlmostEqual(result["priority_score"], 4.0)
        self.assertEqual(result["route"], "P1_ESCALATION")

    def test_priority_score_low(self):
        vis_data = {"damage_severity": 1}
        text_data = {"sentiment_severity": 2}
        
        result = self.engine.calculate_priority_score(vis_data, text_data)
        self.assertEqual(result["route"], "NORMAL_QUEUE")

if __name__ == '__main__':
    unittest.main()
