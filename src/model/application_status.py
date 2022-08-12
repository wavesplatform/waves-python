from enum import Enum


class ApplicationStatus(Enum):

    SUCCEEDED = 'succeeded'
    SCRIPT_EXECUTION_FAILED = 'script_execution_failed'
    UNKNOWN = 'unknown'
