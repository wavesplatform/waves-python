from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json, LetterCase

from waves_python.transaction.transaction_with_status import TransactionWithStatus
from waves_python.model.block_headers import BlockHeaders


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Block(BlockHeaders):
    transactions: List[TransactionWithStatus]
    fee: float
