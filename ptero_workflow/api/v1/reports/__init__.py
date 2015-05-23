from . import workflow_details
from . import workflow_executions
from . import workflow_outputs
from . import workflow_skeleton
from . import workflow_status

_REPORTS = {
    'workflow-details': workflow_details.report,
    'workflow-executions': workflow_executions.report,
    'workflow-outputs': workflow_outputs.report,
    'workflow-skeleton': workflow_skeleton.report,
    'workflow-status': workflow_status.report,
    }

def report_names():
    return _REPORTS.keys()

def get_report_generator(report_type):
    return _REPORTS[report_type]
