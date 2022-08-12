from typing import List

from pydantic import Field

from src.account.address import Address
from src.common.base58_string import Base58String
from src.model.node_model import NodeModel


class BlockHeaders(NodeModel):
    version: int = Field()
    timestamp: float = Field()
    reference: Base58String = Field()
    base_target: float = Field(alias='base-target')
    generation_signature: Base58String = Field(alias='generation-signature"')
    transactions_root: Base58String = Field(alias='transactionsRoot')
    id: Base58String = Field(alias='id')
    features: List[int] = Field()
    desired_reward: float = Field(alias='desiredReward')
    generator: Address = Field()
    signature: Base58String = Field()
    size: int = Field(alias='blocksize')
    transactions_count: int = Field(alias='transactionCount')
    height: int = Field()
    total_fee: float = Field(alias='totalFee')
    reward: float = Field()
    vrf: Base58String = Field(alias='VRF')
