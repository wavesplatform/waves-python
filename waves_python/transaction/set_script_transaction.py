from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction import Transaction


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SetScriptTransaction(Transaction):
    TYPE: int = 13
    LATEST_VERSION: int = 2
    min_fee: float = 1000000
    script: str = ''
