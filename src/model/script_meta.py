from typing import Dict, List

from pydantic import Field

from src.model.arg_meta import ArgMeta
from src.model.node_model import NodeModel


class ScriptMeta(NodeModel):
    meta_version: int = Field(alias='version')
    callable_functions: Dict[str, List[ArgMeta]] = Field(alias='callableFuncTypes')
