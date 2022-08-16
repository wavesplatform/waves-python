from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction_with_status import TransactionWithStatus


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TransactionInfo(TransactionWithStatus):
    height: int = 0
