# from waves_python.transaction.transaction import Transaction
#
#
# class InvokeScriptTransaction(Transaction):
#     pass
from dataclasses import dataclass
from typing import Any, List

from dataclasses_json import dataclass_json, LetterCase

from waves_python.account.address import Address
from waves_python.common.asset_id import AssetId
from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Function:
    name: str
    args: List[str]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Amount:
    value: float
    asset_id: Any

    def __post_init__(self):
        self.asset_id = AssetId(base58_str=self.asset_id)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class InvokeScriptTransaction(Transaction):
    TYPE: int = 16
    LATEST_VERSION: int = 2
    d_app: Any = None
    min_fee: float = 500000
    function: Function = None
    payments: List[Amount] = None
