class SentimentClassifier:
    """
    Mock interface for the NLP component.
    Parses a customer review into numerical severity logic.
    """

    def analyze_text(self, text: str) -> dict:
        """
        Calculates sentiment severity on a 0-5 scale.
        0 = Very Positive, 5 = Very Negative / Extremely Frustrated.
        """
        text_lower = text.lower()
        
        # MOCK IMPLEMENTATION
        # Look for trigger keywords indicating high frustration
        if any(word in text_lower for word in ["demand", "smashed", "unacceptable", "terrible", "falling out"]):
            return {
                "sentiment_category": "Very Negative",
                "sentiment_severity": 5, 
                "requires_human_attention": True
            }
        
        if any(word in text_lower for word in ["bad", "scratched", "disappointed"]):
            return {
                "sentiment_category": "Negative",
                "sentiment_severity": 3,
                "requires_human_attention": False
            }
            
        return {
            "sentiment_category": "Neutral/Positive",
            "sentiment_severity": 0,
            "requires_human_attention": False
        }
