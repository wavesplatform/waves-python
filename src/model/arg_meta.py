from pydantic import Field

from src.model.node_model import NodeModel


class ArgMeta(NodeModel):
    name: str = Field()
    type_name: str = Field(alias='type')
