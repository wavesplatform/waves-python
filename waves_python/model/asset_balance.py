from dataclasses import dataclass
from typing import Optional, Dict

from dataclasses_json import dataclass_json, LetterCase

from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssetBalance(NodeModel):
    asset_id: str
    balance: float
    reissuable: bool
    min_sponsored_asset_fee: Optional[float]
    sponsor_balance: Optional[float]
    quantity: Optional[float]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssetDistribution(NodeModel):
    has_next: bool
    last: str
    values: Dict
