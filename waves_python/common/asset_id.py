from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json, LetterCase

from waves_python.model.node_model import NodeModel

BYTE_LENGTH = 32
WAVES_STRING = "WAVES"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssetId:
    base58_str: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AssetIds(NodeModel):
    ids: List[AssetId]
