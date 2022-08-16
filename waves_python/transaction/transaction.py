from dataclasses import dataclass
from typing import Any, Optional

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction_or_order import TransactionOrOrder


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Transaction(TransactionOrOrder):
    version: Optional[int] = None
    fee: Optional[float] = None
    timestamp: Optional[float] = None
    sender: Optional[Any] = None
    chain_id: Optional[int] = None
    type: Optional[int] = None

