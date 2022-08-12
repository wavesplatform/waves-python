from typing import Dict

from pydantic import Field

from src.common.base64_string import Base64String
from src.model.node_model import NodeModel


class ScriptInfo(NodeModel):
    script: Base64String = Field()
    complexity: int = Field()
    verifier_complexity: int = Field(alias='verifierComplexity')
    callable_complexities: Dict[str, int] = Field(alias='callableComplexities')
    extra_fee: float = Field(alias='extraFee')
