from pydantic import Field

from src.model.node_model import NodeModel


class NodeException(Exception, NodeModel):
    error_code: int = Field(alias='error')
    message: str = Field(alias='message')
