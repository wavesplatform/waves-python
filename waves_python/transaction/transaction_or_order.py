from dataclasses import dataclass
from typing import Any, Optional

from dataclasses_json import dataclass_json, LetterCase

from waves_python.common.id import Id
from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TransactionOrOrder(NodeModel):
    id: Optional[Any] = None
    public_key: Optional[str] = None
    chain_id: Optional[Any] = None

    def __post_init__(self):
        self.id = Id(base58_str=self.id)
