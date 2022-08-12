from pydantic import Field

from src.account.address import Address
from src.model.node_model import NodeModel


class Balance(NodeModel):
    address: Address = Field()
    available: float = Field()
    regular: float = Field()
    generating: float = Field()
    effective: float = Field()
