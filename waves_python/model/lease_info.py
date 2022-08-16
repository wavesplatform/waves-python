from dataclasses import dataclass, field
from typing import Any, Optional

from dataclasses_json import dataclass_json, LetterCase, config

from waves_python.account.address import Address
from waves_python.common.id import Id
from waves_python.model.lease_status import LeaseStatus
from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LeaseInfo(NodeModel):
    lease_id: Any = field(metadata=config(field_name="id"))
    origin_transaction_id: Any
    sender: Any
    recipient: Any
    amount: float
    height: int
    status: LeaseStatus
    cancel_height: Optional[int]
    cancel_transaction_id: Any

    def __post_init__(self):
        self.lease_id = Id(base58_str=self.lease_id)
        self.sender = Address(base58_str=self.sender)
        self.recipient = Address(base58_str=self.recipient)
        self.origin_transaction_id = Id(base58_str=self.origin_transaction_id)
        self.cancel_transaction_id = Id(base58_str=self.cancel_transaction_id)
