<div align="center">
  <h1>🚀 Multimodal Customer Feedback Triage Pipeline</h1>
  <p><b>An n8n-based AI workflow that analyzes customer text feedback and product images to prioritize support escalations.</b></p>
  
  [![n8n](https://img.shields.io/badge/n8n-Workflow_Automation-ff6600?style=for-the-badge&logo=n8n)](https://n8n.io/)
  [![OpenAI](https://img.shields.io/badge/GPT--4o-Vision_&_Sentiment-412991?style=for-the-badge&logo=openai)](https://openai.com/)
  [![Slack](https://img.shields.io/badge/Slack-Automated_Alerts-4A154B?style=for-the-badge&logo=slack)](https://slack.com/)
</div>

<br/>

## 📖 Overview
Normally, companies rely on human agents to manually read through customer emails and visually inspect photos of broken products to prioritize refunds. This project automates the triage workflow by combining image analysis and text sentiment to automatically route support escalations.

### Practical Value
- **Saves Engineering Hours**: Automatically filters out minor issues into routine databases.
- **Reduces Return Fraud**: Cross-references text claims (e.g., "It's shattered!") with actual visual evidence.
- **Fine-Grained Sentiment Classification**: Categorizes feedback into a 5-level sentiment mapping to appropriately weight urgency.

---

## 🏗️ Technical Architecture

This repository bridges **n8n** (an open-source workflow engine) with a **Python** backend.

**Triage Priority Scoring Algorithm:**
Instead of simple boolean triggers, this pipeline parses JSON from the GPT-4o Vision and Sentiment nodes to calculate a weighted urgency score:

```python
priority_score = (0.5 * damage_severity) + (0.3 * sentiment_severity) + (0.2 * claim_alignment)
```
*Scores `>= 3.5` trigger an immediate P1 Slack Alert. Lower scores are queued into Notion.*

---

## 📊 Example Payload

### A. Example Input
```json
{
  "review_text": "The product arrived broken and unusable. I am extremely frustrated.",
  "image_url": "https://example.com/damaged-item.jpg"
}
```

### B. Example Output
```json
{
  "defect_detected": true,
  "defect_type": "screen crack",
  "visual_evidence_score": 9,
  "sentiment_label": "Very Negative",
  "priority_score": 4.7,
  "route": "P1 Slack Escalation"
}
```

---

## 🧠 Structured Output Schema
The AI Nodes guarantee structured generation using the following JSON schema:
```json
{
  "defect_detected": "boolean",
  "defect_type": "string",
  "visual_evidence_score": "integer",
  "text_sentiment": "string",
  "priority_score": "float"
}
```

---

## 🚀 Repository Structure

```text
multimodal-feedback-pipeline/
├── app/
│   ├── analyze_feedback.py       # Main orchestration script
│   ├── fusion_logic.py           # Priority scoring algorithm
│   ├── image_damage_checker.py   # Vision API interface
│   ├── sentiment_classifier.py   # Text analysis interface
│   └── sample_payloads.json      # Mock input/output examples
├── assets/
│   ├── workflow-diagram.png      
│   └── sample-alert.png         
├── tests/
│   └── test_fusion_logic.py      # Unit tests for scoring bounds
├── workflow.json                 # n8n Pipeline Export
└── README.md
```

## ⚠️ Limitations
- **Image Quality Constraints:** Dependent on user-submitted photo lighting and resolution.
- **Vision Model Variability:** LLM visual reasoning bounds are non-deterministic.
- **No Benchmark Dataset:** Currently functional as a logic design pattern, not yet tuned on a production fraud dataset.
- Designed as a structured workflow demonstration, not an end-to-end production model.

---
<div align="center">
  <i>Developed by <b>Sai pavan</b></i>
</div>
