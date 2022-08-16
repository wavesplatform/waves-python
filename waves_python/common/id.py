from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json, LetterCase

from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Id(NodeModel):
    base58_str: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Ids(NodeModel):
    ids: List[Id]
