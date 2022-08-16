from dataclasses import dataclass
from typing import List, Dict

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class DataTransaction(Transaction):
    TYPE: int = 12
    LATEST_VERSION: int = 2
    MIN_FEE: int = 100000
    data: List[Dict] = None
