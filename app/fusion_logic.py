class TriageFusionEngine:
    """
    Core business logic for combining Vision and NLP outputs.
    Calculates the final priority score for support escalation.
    """

    def __init__(self, damage_weight=0.5, sentiment_weight=0.3, claim_match_weight=0.2):
        self.weights = {
            "damage": damage_weight,
            "sentiment": sentiment_weight,
            "claim_match": claim_match_weight
        }

    def assess_claim_match(self, damage_score: int, sentiment_score: int) -> int:
        """
        Determines the likelihood that the user is exaggerating or lying.
        Returns a risk score 0-5.
        """
        if sentiment_score >= 4 and damage_score == 0:
            return 5 # Very likely mismatched claim
        if sentiment_score >= 3 and damage_score <= 1:
            return 3 # Moderate risk 
        return 0 # Claims align with visual evidence
        
    def calculate_priority_score(self, visual_data: dict, text_data: dict) -> dict:
        """
        Computes the Triage Score based on the formula:
        priority_score = 0.5 * damage_score + 0.3 * sentiment_score + 0.2 * claim_match_score
        """
        damage_score = visual_data.get("damage_severity", 0)
        sentiment_score = text_data.get("sentiment_severity", 0)
        
        claim_match_score = self.assess_claim_match(damage_score, sentiment_score)
        
        # Calculate weighted priority (Max possible score is 5.0)
        priority_score = (
            (self.weights["damage"] * damage_score) + 
            (self.weights["sentiment"] * sentiment_score) + 
            (self.weights["claim_match"] * claim_match_score)
        )
        
        # Determine Routing Action
        if priority_score >= 4.0:
            action = "P1_ESCALATION"
        elif priority_score >= 2.5:
            action = "P2_ESCALATION"
        else:
            action = "NORMAL_QUEUE"
                
        return {
            "damage_score": damage_score,
            "sentiment_score": sentiment_score,
            "claim_match_score": claim_match_score,
            "priority_score": round(priority_score, 2),
            "route": action
        }
