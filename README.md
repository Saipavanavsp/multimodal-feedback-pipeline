# Multimodal Customer Feedback Triage Pipeline

**An n8n-based AI workflow that analyzes customer text feedback and product images to prioritize support escalations.**

## 📖 Problem Solved
Customer support teams currently rely on human agents to manually read through complaint emails and visually inspect photos of broken products. This project automates the triage process by combining text sentiment classification and image analysis to automatically route escalations, saving engineering hours and reducing return fraud.

---

## 🏗️ Technical Architecture & Logic

This repository bridges **n8n** (workflow orchestration) with a Python-based scoring backend.

**Priority Scoring Engine:**
The pipeline parses JSON from the Vision and Sentiment models to calculate a weighted urgency score:

```python
priority_score = (0.5 * damage_score) + (0.3 * sentiment_score) + (0.2 * claim_match_score)
```

**Routing Rules:**
- `>= 4.0` → **P1 Escalation** (Sent to Slack)
- `2.5 to 3.9` → **P2 Escalation** (Sent to Slack)
- `< 2.5` → **Routine queue** (Logged to Notion/Database)

---

## 📊 Sample Payloads

**Sample Input**
```json
{
  "review_text": "The product arrived broken and unusable.",
  "image_url": "https://example.com/damaged-item.jpg"
}
```

**Sample Output**
```json
{
  "defect_detected": true,
  "defect_type": "screen crack",
  "visual_evidence_score": 9,
  "sentiment_label": "Very Negative",
  "claim_match_score": 4,
  "priority_score": 4.7,
  "route": "P1 Slack Escalation"
}
```

**Structured Output Schema**
```json
{
  "defect_detected": true,
  "defect_type": "cracked_screen",
  "visual_evidence_score": 8,
  "sentiment_label": "Very Negative",
  "priority_score": 4.6,
  "route": "P1 Slack Escalation"
}
```

---

## 📈 Evaluation & Metrics
A baseline evaluation of the logic model on simulated edge cases:

| Test Case | Expected | Output | Result |
| :--- | :--- | :--- | :--- |
| Broken item + angry review | P1 | P1 | Pass |
| Minor scratch + neutral review | P2 | P2 | Pass |
| No visible defect + negative review | Routine queue | Routine queue | Pass |

---

## 🚀 Repository Structure

```text
multimodal-feedback-pipeline/
├── app/
│   ├── fusion_logic.py           
│   ├── schemas.py                
│   ├── image_damage_checker.py   
│   ├── sentiment_classifier.py   
│   └── sample_payloads.json      
├── assets/
│   ├── workflow-diagram.png      
│   ├── n8n-workflow-screenshot.png
│   ├── sample-json-output.png
│   └── slack-alert-example.png         
├── tests/
│   └── test_fusion_logic.py      
├── .env.example
├── requirements.txt
├── workflow.json                 
├── README.md
└── LICENSE
```

---

## ⚠️ Limitations
- **Dependent on image quality and lighting**
- **LLM vision outputs may vary across edge cases**
- **No benchmark dataset yet for false positive/false negative measurement**
- **Current version is a workflow prototype**, not a production fraud-detection system
- **Rule thresholds are heuristic** and should be tuned with real support data

---

## 🔮 Future Improvements
1. Replace rule-based routing with learned risk scoring trained on historical tickets.
2. Add OCR extraction from invoice / warranty cards.
3. Add specialized image-text contradiction detection patterns.
4. Store outcomes in a relational database for root-cause analytics.
5. Build a dashboard for escalation trends.
6. Add confidence thresholds that route low-confidence AI decisions to a human-in-the-loop fallback queue.
