# Multimodal Customer Feedback Triage Pipeline

**An AI-assisted multimodal workflow that analyzes customer text feedback and product images to prioritize support escalations.**

Traditionally, companies rely on human agents to manually read through customer emails and visually inspect photos of broken products to prioritize refunds. This project automates the triage workflow by evaluating unstructured data (Computer Vision + Natural Language Processing) and mathematically determining a priority score for escalation.

## 🏗️ Technical Architecture

This repository bridges **n8n** (an open-source workflow engine) with a **Python ML service** backend.

**Triage Priority Scoring Algorithm:**
Instead of simple boolean triggers, this pipeline relies on structured parsing to calculate a weighted urgency score:

```python
priority_score = (0.5 * damage_severity) + (0.3 * sentiment_severity) + (0.2 * fraud_risk)
```
*Scores `>= 3.5` trigger an immediate P1 Slack Alert. Lower scores are queued into Notion.*

**Data Flow:**
1. **The Input**: A simulated customer form provides `review_text` and an `image_url`.
2. **The Visual Assessment**: A Vision node inspects the image for physical damage, outputting a severity rating (0-5). 
3. **The Sentiment Assessment**: A NLP node reads the `review_text`, identifying frustration and mapping it to a severity rating (0-5).
4. **Fraud Detection**: The python backend cross-references the text claims with the visual reality (e.g., "Shattered screen" vs pristine image) to assign a fraud risk severity.
5. **Score Fusion**: The `fusion_logic.py` core calculates the final priority score.
6. **The Action**: Triage routing to Slack or Database.

## 🚀 Repository Structure

```text
├── README.md
├── workflow.json                 # n8n Pipeline Export
├── app/
│   ├── analyze_feedback.py       # Main orchestration script
│   ├── fusion_logic.py           # Priority scoring algorithm
│   ├── image_damage_checker.py   # Vision API interface
│   ├── sentiment_classifier.py   # Text analysis interface
│   └── sample_payloads.json      # Mock input/output examples
└── tests/
    └── test_fusion_logic.py      # Unit tests for threshold accuracy
```

## 🧠 Sample Payload

**Input parameters:**
```json
{
  "image_url": "https://example.com/cracked_screen.jpg",
  "review_text": "My phone arrived completely smashed and the screen is falling out. I demand a refund immediately!"
}
```

**Fusion Output (Calculated via `app/fusion_logic.py`):**
```json
{
  "damage_severity": 4, 
  "sentiment_severity": 5, 
  "fraud_risk": 0,
  "final_priority_score": 3.5,
  "action": "TRIGGER_P1_ALERT"
}
```

---
<div align="center">
  <i>Developed by <b>Sai pavan</b> for ML Engineering Portfolio Assessment</i>
</div>
