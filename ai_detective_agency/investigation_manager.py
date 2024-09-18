## investigation_manager.py
from typing import Dict
from case import CaseManager
from ai_models import AIModelManager

class InvestigationManager:
    def __init__(self):
        self.case_manager = CaseManager()
        self.ai_model_manager = AIModelManager()

    def create_case(self, case_data: Dict) -> str:
        return self.case_manager.create_case(case_data)

    def assign_ai_models(self, case_id: str) -> None:
        # This function is a placeholder to demonstrate how AI models could be assigned.
        # In a real-world scenario, this function would contain logic to assign specific
        # AI models to a case based on the case details or requirements.
        pass

    def collect_evidence(self, case_id: str, evidence_data: Dict) -> None:
        case = self.case_manager.get_case(case_id)
        if case:
            case.add_evidence(evidence_data)

    def generate_report(self, case_id: str) -> str:
        case = self.case_manager.get_case(case_id)
        if case:
            report = case.generate_report()
            return report.summarize_findings()
        else:
            raise ValueError(f"No case found with ID: {case_id}")

    def run_investigation(self, case_id: str, evidence_data: Dict) -> None:
        self.ai_model_manager.load_models()
        findings = self.ai_model_manager.run_investigation(case_id, evidence_data)
        case = self.case_manager.get_case(case_id)
        if case:
            for evidence_id, finding in findings.items():
                case.evidence.append(finding)
            case.generate_report()
        else:
            raise ValueError(f"No case found with ID: {case_id}")
