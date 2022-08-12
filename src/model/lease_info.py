from pydantic import Field

from src.account.address import Address
from src.common.id import Id
from src.common.recipient import Recipient
from src.model.lease_status import LeaseStatus
from src.model.node_model import NodeModel


class LeaseInfo(NodeModel):
    lease_id: Id = Field(alias='id')
    origin_transaction_id: Id = Field(alias='originTransactionId')
    sender: Address = Field()
    recipient: Recipient = Field()
    amount: float = Field()
    height: int = Field()
    status: LeaseStatus = Field()
    cancel_height: int = Field(alias='cancelHeight')
    cancel_transaction_id: Id = Field(alias='cancelTransactionId')
