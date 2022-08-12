from typing import Optional

from pydantic import Field

from src.model.node_model import NodeModel


class AssetBalance(NodeModel):
    asset_id: str = Field(alias='assetId')
    balance: Optional[float] = Field()
    reissuable: Optional[bool] = Field()
    min_sponsored_asset_fee: Optional[float] = Field(alias='minSponsoredAssetFee')
    sponsor_balance: Optional[float] = Field(alias='sponsorBalance')
    quantity: Optional[float] = Field()

    class Config:
        arbitrary_types_allowed = True
