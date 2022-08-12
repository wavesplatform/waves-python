from pydantic import Field

from src.model.node_model import NodeModel


class Votes(NodeModel):
    increase: int = Field()
    decrease: int = Field()
