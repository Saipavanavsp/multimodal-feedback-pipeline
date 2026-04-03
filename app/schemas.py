from pydantic import BaseModel
from typing import Optional

class EscallationOutputSchema(BaseModel):
    defect_detected: bool
    defect_type: Optional[str] = None
    visual_evidence_score: int
    sentiment_label: str
    claim_match_score: int
    priority_score: float
    route: str
