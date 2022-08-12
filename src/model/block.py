from typing import List

from pydantic import Field

from src.info.transaction_with_status import TransactionWithStatus
from src.model.block_headers import BlockHeaders


class Block(BlockHeaders):
    transactions: List[TransactionWithStatus] = Field()
    fee: float = Field()
