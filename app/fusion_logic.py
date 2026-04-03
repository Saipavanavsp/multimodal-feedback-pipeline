class TriageFusionEngine:
    """
    Core business logic for combining Vision and NLP outputs.
    Calculates the final priority score for support escalation.
    """

    def __init__(self, damage_weight=0.5, sentiment_weight=0.3, fraud_weight=0.2):
        self.weights = {
            "damage": damage_weight,
            "sentiment": sentiment_weight,
            "fraud": fraud_weight
        }

    def assess_fraud_risk(self, damage_severity: int, sentiment_severity: int) -> int:
        """
        Determines the likelihood that the user is exaggerating or lying.
        Example: High sentiment severity (very angry) but 0 physical damage.
        Returns a risk score 0-5.
        """
        if sentiment_severity >= 4 and damage_severity == 0:
            return 5 # Very likely fraud or completely mismatched claim
        if sentiment_severity >= 3 and damage_severity <= 1:
            return 3 # Moderate risk 
        return 0 # Claims align with visual evidence
        
    def calculate_priority_score(self, visual_data: dict, text_data: dict) -> dict:
        """
        Computes the Triage Score based on the formula:
        priority = (0.5*damage) + (0.3*sentiment) + (0.2*fraud_risk)
        """
        damage = visual_data.get("damage_severity", 0)
        sentiment = text_data.get("sentiment_severity", 0)
        
        fraud_risk = self.assess_fraud_risk(damage, sentiment)
        
        # Calculate weighted priority (Max possible score is 5.0)
        priority_score = (
            (self.weights["damage"] * damage) + 
            (self.weights["sentiment"] * sentiment) + 
            (self.weights["fraud"] * fraud_risk)
        )
        
        # Determine Routing Action
        action = "LOG_TO_NOTION"
        if priority_score >= 3.5:
            if fraud_risk >= 4:
                action = "FLAG_FOR_FRAUD_REVIEW"
            else:
                action = "TRIGGER_P1_ALERT"
                
        return {
            "damage_severity": damage,
            "sentiment_severity": sentiment,
            "fraud_risk": fraud_risk,
            "final_priority_score": round(priority_score, 2),
            "action": action
        }
