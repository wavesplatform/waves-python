from dataclasses import dataclass
from typing import Optional, Any

from dataclasses_json import dataclass_json, LetterCase

from waves_python.account.address import Address
from waves_python.common.asset_id import AssetId
from waves_python.common.id import Id
from waves_python.model.node_model import NodeModel
from waves_python.model.script_details import ScriptDetails


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssetDetails(NodeModel):
    asset_id: Any
    issue_height: int
    issue_timestamp: float
    issuer: Any
    issuer_public_key: str
    name: str
    description: str
    decimals: int
    reissuable: bool
    quantity: float
    scripted: bool
    min_sponsored_asset_fee: Optional[float]
    origin_transaction_id: Any
    script_details: Optional[ScriptDetails] = None

    def __post_init__(self):
        self.asset_id = AssetId(base58_str=self.asset_id)
        self.issuer = Address(base58_str=self.issuer)
        self.origin_transaction_id = Id(base58_str=self.origin_transaction_id)
