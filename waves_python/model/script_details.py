from dataclasses import field, dataclass
from dataclasses_json import config, dataclass_json, LetterCase

from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ScriptDetails(NodeModel):
    script: str
    complexity: int = field(metadata=config(field_name="scriptComplexity"))
