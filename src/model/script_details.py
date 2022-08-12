from pydantic import Field

from src.common.base64_string import Base64String
from src.model.node_model import NodeModel


class ScriptDetails(NodeModel):
    script: Base64String = Field()
    complexity: int = Field(alias='scriptComplexity')
