from pydantic import Field

from src.model.node_model import NodeModel


class HistoryBalance(NodeModel):
    height: int = Field()
    balance: float = Field()
