from dataclasses import dataclass
from typing import Any

from dataclasses_json import dataclass_json, LetterCase

from waves_python.common.id import Id
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LeaseCancelTransaction(Transaction):
    TYPE: int = 9
    LATEST_VERSION: int = 3
    min_fee: float = 100000
    lease_id: Any = None

    def __post_init__(self):
        self.lease_id = Id(base58_str=self.lease_id)
