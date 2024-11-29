## case.py
from typing import List, Dict
from evidence import Evidence
from report import Report

class Case:
    def __init__(self, case_id: str, details: Dict):
        self.case_id: str = case_id
        self.details: Dict = details
        self.evidence: List[Evidence] = []
        self.report: Report = None

    def add_evidence(self, evidence_data: Dict) -> None:
        new_evidence = Evidence(evidence_id=evidence_data['evidence_id'],
                                type=evidence_data['type'],
                                data=evidence_data['data'])
        self.evidence.append(new_evidence)

    def generate_report(self) -> Report:
        findings = {e.evidence_id: e.data for e in self.evidence}
        self.report = Report(report_id=self.case_id, findings=findings)
        return self.report

class CaseManager:
    def __init__(self):
        self.cases: Dict[str, Case] = {}

    def create_case(self, case_data: Dict) -> str:
        new_case = Case(case_id=case_data['case_id'], details=case_data['details'])
        self.cases[case_data['case_id']] = new_case
        return new_case.case_id

    def get_case(self, case_id: str) -> Case:
        return self.cases.get(case_id)
