from __future__ import annotations

from dataclasses import dataclass
from typing import List, Any, Optional, Dict

from dataclasses_json import dataclass_json, LetterCase

from waves_python.model.node_model import NodeModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Address(NodeModel):
    base58_str: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AddressList(NodeModel):
    addresses: List[str]
    height: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AddressBalance(NodeModel):
    address: str
    regular: int
    generating: int
    available: int
    effective: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AddressData(NodeModel):
    key: Optional[str]
    type: Optional[Any]
    value: Optional[Any]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AddressKeys(NodeModel):
    keys: List[str]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AddressScriptInfo(NodeModel):
    address: str
    script: str
    scriptText: str
    complexity: int
    verifierComplexity: int
    callableComplexities: Dict
    extraFee: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AddressScriptInfoMeta(NodeModel):
    address: str
    meta: Dict
