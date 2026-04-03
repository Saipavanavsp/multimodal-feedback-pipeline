<div align="center">
  <h1>🚀 Multi-Modal Feedback Pipeline</h1>
  <p><b>An AI-Powered Sensor Fusion Application for Automated Customer Support Escalations</b></p>
  
  [![n8n](https://img.shields.io/badge/n8n-Workflow_Automation-ff6600?style=for-the-badge&logo=n8n)](https://n8n.io/)
  [![OpenAI](https://img.shields.io/badge/GPT--4o-Vision_&_Sentiment-412991?style=for-the-badge&logo=openai)](https://openai.com/)
  [![Slack](https://img.shields.io/badge/Slack-Automated_Alerts-4A154B?style=for-the-badge&logo=slack)](https://slack.com/)
</div>

<br/>

## 📖 Executive Summary
Traditionally, companies rely on human agents to manually read through customer emails and visually inspect photos of broken products to prioritize refunds. This traditional process is slow, prone to bias, and vulnerable to return fraud.

This project **automates the triage workflow** by implementing **Sensor Fusion**: it combines Computer Vision (evaluating photo evidence) and Natural Language Processing (assessing text sentiment) to automatically trigger priority escalations.

### 💡 The Value Proposition
- **Saves Hundreds of Hours**: Automatically filters out minor issues into routine databases.
- **Prevents Refund Fraud**: Cross-references text claims (e.g., "It's shattered!") with actual visual evidence.
- **Micro-Targeted Sentiment**: Categorizes feedback into 5 granular emotional brackets, far superior to basic positive/negative mapping.

---

## 🏗️ Technical Architecture

Built purely with **n8n** (an open-source workflow engine), this pipeline connects raw inbound webhooks directly to specialized AI agents.

**Data Flow:**
1. **The Input (Webhook)**: A simulated web form submission (`POST` request) supplies two parameters: `review_text` and `image_url`.
2. **Data Extraction**: An HTTP Request node converts the image URL into a binary stream, allowing the Vision model to "see" it without hosting constraints.
3. **The Visual Check**: A `GPT-4o` Vision Node inspects the image for physical damage and returns a strict JSON payload.
4. **The Emotional Check**: A specialized Sentiment node reads the `review_text`, mapping the frustration level into 5 granular brackets (`Very Positive`, `Positive`, `Neutral`, `Negative`, `Very Negative`).
5. **Sensor Fusion (Merge)**: A Merge node synchronizes the data streams, combining the visual assessment JSON with the emotional assessment JSON.
6. **The Action (IF Routing)**: If `Damage == True` AND `Emotion == Very Negative`, the system instantly triggers a **Priority 1 (P1) Slack Alert** to the Quality Control team. Otherwise, it logs to Notion for routine review.

---

## 🚀 Setup & Installation (Import Guide)

This repository includes the raw JSON structure required to deploy the exact node architecture used in this pipeline.

### Prerequisites
- An active [n8n](https://n8n.io/) instance (Cloud or Self-Hosted).
- An OpenAI API Key (with GPT-4o access).
- A Slack Workspace (for testing the webhooks/alerts).

### Instructions
1. Download or copy the contents of `workflow.json` located in this repository.
2. Open your n8n workspace, navigate to the workflows canvas, and select **Import from File** (or simply paste the JSON over the canvas).
3. Open the **Vision AI** and **Sentiment AI** nodes to link your OpenAI credentials.
4. Open the **Slack** node to link your workspace token and select a target channel.
5. Save and Activate the workflow.
6. Use an API client (like Postman) to send a `POST` request to your Webhook Test URL containing sample `image_url` and `review_text` values.

---

## 🧠 System Prompts Used

This project uses rigorous prompt engineering to guarantee structured JSON outputs suitable for computational branching.

### The Master Vision Assessor Prompt
```json
Role: You are an AI Quality Assurance Inspector.
Context: A customer submitted a text review and a photo of a product.
Mission: 
1. Image check: Is there a functional or cosmetic defect?
2. Text check: How intense is the customer's frustration?
3. Cross-Reference: Does the text claim match the visual evidence?

Output as Strict JSON:
{
  "defect_detected": true,
  "defect_type": "string",
  "visual_evidence_score": 10, 
  "text_visual_alignment": "Match",
  "urgency_level": "High"
}
```

---
<div align="center">
  <i>Developed by <b>Sai pavan</b> for AI/ML Portfolio Assessment</i>
</div>
