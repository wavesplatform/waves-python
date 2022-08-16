from dataclasses import dataclass
from typing import Any

from dataclasses_json import LetterCase, dataclass_json

from waves_python.account.address import Address
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LeaseCancelTransaction(Transaction):
    TYPE: int = 8
    LATEST_VERSION: int = 3
    min_fee: float = 100000
    recipient: Any = None
    amount: float = 0

    def __post_init__(self):
        self.recipient = Address(base58_str=self.recipient)
