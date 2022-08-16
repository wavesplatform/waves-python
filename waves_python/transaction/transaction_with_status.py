from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from waves_python.model.application_status import ApplicationStatus
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TransactionWithStatus(Transaction):
    application_status: ApplicationStatus = ApplicationStatus.SUCCEEDED
