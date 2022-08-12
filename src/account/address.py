from __future__ import annotations
from typing import List, Any, Optional, Dict

from pydantic import Field

from src.model.node_model import NodeModel
from src.util import base58_utils


class Address:
    base58_string = Field()

    @classmethod
    def from_str(cls, encoded: str):
        address = cls()
        address.base58_string = base58_utils.from_string(encoded)
        return address

    def to_str(self):
        return base58_utils.to_string(self.base58_string)


class AddressList(NodeModel):
    addresses: List[str]
    height: int


class AddressBalance(NodeModel):
    address: str
    regular: int
    generating: int
    available: int
    effective: int


class AddressData(NodeModel):
    key: Optional[str] = None
    type: Optional[Any] = None
    value: Optional[Any] = None


class AddressKeys(NodeModel):
    keys: List[str]


class AddressScriptInfo(NodeModel):
    address: str
    script: str
    scriptText: str
    complexity: int
    verifierComplexity: int
    callableComplexities: Dict
    extraFee: int


class AddressScriptInfoMeta(NodeModel):
    address: str
    meta: Dict
