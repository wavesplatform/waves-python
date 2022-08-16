from dataclasses import dataclass
from typing import Any

from dataclasses_json import dataclass_json, LetterCase

from waves_python.account.address import Address
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GenesisTransaction(Transaction):
    TYPE: int = 1
    LATEST_VERSION: int = 1
    recipient: Any = None
    amount: float = 0

    def __post_init__(self):
        self.recipient = Address(base58_str=self.recipient)
