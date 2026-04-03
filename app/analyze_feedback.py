import json
from image_damage_checker import ImageDamageChecker
from sentiment_classifier import SentimentClassifier
from fusion_logic import TriageFusionEngine

def run_pipeline(payload_path="app/sample_payloads.json"):
    """
    Main orchestrator demonstrating the multimodal ML pipeline.
    """
    vision_model = ImageDamageChecker()
    nlp_model = SentimentClassifier()
    fusion_engine = TriageFusionEngine()

    with open(payload_path, "r") as f:
        payloads = json.load(f)

    results = []
    
    print("--- Starting Multimodal Feedback Analysis ---\n")
    
    for item in payloads:
        print(f"Scenario: {item['scenario']}")
        print(f"Review: '{item['review_text']}'")
        
        # Phase 1: Visual Extraction
        vis_data = vision_model.analyze_image(item["image_url"])
        
        # Phase 2: NLP Extraction
        text_data = nlp_model.analyze_text(item["review_text"])
        
        # Phase 3: Sensor Fusion / Priority Calculation
        final_assessment = fusion_engine.calculate_priority_score(vis_data, text_data)
        
        print(f"Output: {json.dumps(final_assessment, indent=2)}\n")
        print("-" * 45 + "\n")
        
        results.append({
            "scenario": item["scenario"],
            "assessment": final_assessment
        })
        
    return results

if __name__ == "__main__":
    # Ensure running from root for relative path or adjust locally.
    try:
        run_pipeline("app/sample_payloads.json")
    except FileNotFoundError:
        run_pipeline("sample_payloads.json")
