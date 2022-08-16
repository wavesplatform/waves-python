from dataclasses import dataclass
from typing import Any

from dataclasses_json import dataclass_json, LetterCase

from waves_python.common.asset_id import AssetId
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UpdateAssetInfoTransaction(Transaction):
    TYPE: int = 17
    LATEST_VERSION: int = 1
    min_fee: float = 100000
    asset_id: Any = None
    name: str = ''
    description: str = ''

    def __post_init__(self):
        self.asset_id = AssetId(base58_str=self.asset_id)
