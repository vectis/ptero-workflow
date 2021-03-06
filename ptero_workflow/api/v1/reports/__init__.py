from . import limited_workflow_executions
from . import limited_workflow_status_updates
from . import spawned_workflows
from . import workflow_details
from . import workflow_executions
from . import workflow_outputs
from . import workflow_skeleton
from . import workflow_status
from . import workflow_summary
from . import workflow_submission_data
from ptero_common.exceptions import NoSuchEntityError

_REPORTS = {
    'limited-workflow-executions': limited_workflow_executions.report,
    'limited-workflow-status-updates': limited_workflow_status_updates.report,
    'spawned-workflows': spawned_workflows.report,
    'workflow-details': workflow_details.report,
    'workflow-executions': workflow_executions.report,
    'workflow-outputs': workflow_outputs.report,
    'workflow-skeleton': workflow_skeleton.report,
    'workflow-status': workflow_status.report,
    'workflow-summary': workflow_summary.report,
    'workflow-submission-data': workflow_submission_data.report,
    }


def report_names():
    return _REPORTS.keys()


def get_report_generator(report_type):
    try:
        return _REPORTS[report_type]
    except KeyError:
        raise NoSuchEntityError('Report Type (%s) is invalid' % report_type)
