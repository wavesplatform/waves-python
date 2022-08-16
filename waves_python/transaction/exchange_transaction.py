from dataclasses import dataclass
from typing import List, Dict

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExchangeTransaction(Transaction):
    TYPE: int = 7
    LATEST_VERSION: int = 3
    MIN_FEE: int = 300000
    amount: float = 0
    price: float = 0
    buy_matcher_fee: float = 0
    sell_matcher_fee: float = 0
    orders: List[Dict] = None
