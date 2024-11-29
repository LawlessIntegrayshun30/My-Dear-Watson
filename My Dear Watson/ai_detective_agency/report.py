## report.py
from typing import Dict

class Report:
    def __init__(self, report_id: str, findings: Dict[str, Dict]):
        self.report_id: str = report_id
        self.findings: Dict[str, Dict] = findings

    def create_report(self, findings: Dict[str, Dict]) -> None:
        """
        Create a report with the given findings. This method updates the
        report's findings with the provided data.

        :param findings: A dictionary containing the findings of the investigation.
        """
        self.findings = findings

    def summarize_findings(self) -> str:
        """
        Summarize the findings in a human-readable format.

        :return: A string that summarizes the findings of the report.
        """
        summary = f"Report ID: {self.report_id}\n"
        summary += "Findings:\n"
        for evidence_id, finding in self.findings.items():
            summary += f"Evidence ID: {evidence_id}\n"
            for key, value in finding.items():
                summary += f"  {key}: {value}\n"
        return summary
