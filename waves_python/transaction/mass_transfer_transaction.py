from dataclasses import dataclass
from typing import Any, List

from dataclasses_json import dataclass_json, LetterCase

from waves_python.account.address import Address
from waves_python.common.asset_id import AssetId
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Transfer:
    recipient: Any
    amount: float

    def __post_init__(self):
        self.recipient = Address(base58_str=self.recipient)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class MassTransferTransaction(Transaction):
    TYPE: int = 11
    LATEST_VERSION: int = 2
    min_fee: float = 100000
    transfers: List[Transfer] = None
    asset_id: Any = None
    attachment: str = ''

    def __post_init__(self):
        self.asset_id = AssetId(base58_str=self.asset_id)
