from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Votes(NodeModel):
    increase: int
    decrease: int
