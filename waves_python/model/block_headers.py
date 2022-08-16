from dataclasses import dataclass, field
from typing import List, Any

from dataclasses_json import dataclass_json, LetterCase, config

from waves_python.account.address import Address
from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BlockNxtConsensus(NodeModel):
    base_target: float = field(metadata=config(field_name="base-target"))
    generation_signature: str = field(metadata=config(field_name="generation-signature"))


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BlockHeaders(NodeModel):
    version: int
    timestamp: float
    reference: str
    nxt_consensus: BlockNxtConsensus = field(metadata=config(field_name="nxt-consensus"))
    transactions_root: str
    id: str
    features: List[int]
    desired_reward: float
    generator: Any
    signature: str
    size: int = field(metadata=config(field_name="blocksize"))
    transaction_count: int
    height: int
    total_fee: float
    reward: float
    vrf: str = field(metadata=config(field_name="VRF"))

    def __post_init__(self):
        self.generator = Address(base58_str=self.generator)
