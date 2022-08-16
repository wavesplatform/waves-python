from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class MassTransferTransaction(Transaction):
    TYPE: int = 5
    LATEST_VERSION: int = 3
    min_fee: float = 100000
    amount: float = 0
    reissuable: bool = False
