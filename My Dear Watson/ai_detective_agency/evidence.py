## evidence.py
class Evidence:
    def __init__(self, evidence_id: str, evidence_type: str, data: dict):
        self.evidence_id: str = evidence_id
        self.type: str = evidence_type
        self.data: dict = data
