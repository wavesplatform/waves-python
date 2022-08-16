from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BurnTransaction(Transaction):
    TYPE: int = 6
    LATEST_VERSION: int = 3
    MIN_FEE: int = 100000
    amount: float = 0

