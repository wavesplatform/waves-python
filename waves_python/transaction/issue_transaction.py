from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json

from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class IssueTransaction(Transaction):
    TYPE: int = 3
    LATEST_VERSION: int = 3
    min_fee: float = 100000000
    nft_min_fee: float = 100000
    name: bytearray = None
    description: bytearray = None
    quantity: float = 0
    decimals: int = 0
    is_reissuable: bool = False
    script: str = ''
