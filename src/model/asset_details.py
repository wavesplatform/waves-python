from pydantic import Field

from src.account.address import Address
from src.account.public_key import PublicKey
from src.common.asset_id import AssetId
from src.common.id import Id
from src.model.node_model import NodeModel
from src.model.script_details import ScriptDetails


class AssetDetails(NodeModel):
    asset_id: AssetId = Field(alias='assetId')
    issue_height: int = Field(alias='issueHeight')
    issue_timestamp: float = Field(alias='issueTimestamp')
    issuer: Address = Field()
    issuer_public_key: PublicKey = Field(alias='issuerPublicKey')
    name: str = Field()
    description: str = Field()
    decimals: int = Field()
    reissuable: bool = Field()
    quantity: float = Field()
    scripted: bool = Field()
    min_sponsored_asset_fee: float = Field(alias='minSponsoredAssetFee')
    origin_transaction_id: Id = Field(alias='originTransactionId')
    script_details: ScriptDetails = Field(alias='scriptDetails')
