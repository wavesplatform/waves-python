from pydantic import Field

from src.account.address import Address
from src.model.node_model import NodeModel


class Balance(NodeModel):
    address: Address = Field(alias='id')
    balance: float = Field()
