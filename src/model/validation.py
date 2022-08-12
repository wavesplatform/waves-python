from pydantic import Field

from src.model.node_model import NodeModel


class Validation(NodeModel):
    valid: bool = Field()
    validation_time: float = Field(alias='validationTime')
    error: str = Field()
