from dataclasses import dataclass
from typing import Any

from dataclasses_json import dataclass_json, LetterCase

from waves_python.common.asset_id import AssetId
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SponsorFeeTransaction(Transaction):
    TYPE: int = 14
    LATEST_VERSION: int = 2
    min_fee: float = 100000
    asset_id: Any = None
    min_sponsored_fee: float = 100000

    def __post_init__(self):
        self.asset_id = AssetId(base58_str=self.asset_id)
