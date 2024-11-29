## main.py
from investigation_manager import InvestigationManager

def main() -> str:
    # Create an instance of the InvestigationManager
    investigation_manager = InvestigationManager()

    # Example case data (would be provided by some external source in a real scenario)
    case_data = {
        'case_id': 'C001',
        'details': {
            'description': 'Example case description',
            'involved_parties': ['Party1', 'Party2'],
            'date': '2023-01-01'
        }
    }

    # Create a new case
    case_id = investigation_manager.create_case(case_data)

    # Example evidence data (would be provided by some external source in a real scenario)
    evidence_data = {
        'E001': {
            'type': 'text',
            'data': {
                'text': 'Example text evidence'
            }
        },
        'E002': {
            'type': 'image',
            'data': {
                'image': b'Example binary image data'
            }
        }
    }

    # Collect evidence for the case
    for evidence_id, data in evidence_data.items():
        investigation_manager.collect_evidence(case_id, {'evidence_id': evidence_id, 'type': data['type'], 'data': data['data']})

    # Run the investigation (analyze evidence using AI models)
    investigation_manager.run_investigation(case_id, evidence_data)

    # Generate and retrieve the investigation report
    report = investigation_manager.generate_report(case_id)

    return report

if __name__ == '__main__':
    # Run the main function and print the report
    investigation_report = main()
    print(investigation_report)
