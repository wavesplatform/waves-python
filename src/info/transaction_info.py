from abc import ABC
from typing import Type

from src.info.transaction_with_status import TransactionWithStatus
from src.model.application_status import ApplicationStatus
from src.transaction.genesis_transaction import GenesisTransaction
from src.transaction.transaction import Transaction


class TransactionInfo(TransactionWithStatus, ABC):

    def __init__(self, tx: Transaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status)
        self.__height = 1 if height == 0 and tx.type() == GenesisTransaction.TYPE else height

    @property
    def height(self) -> int:
        return self.__height

    def __eq__(self, obj):
        if self == obj:
            return True
        if obj is None or not isinstance(obj, self.__class__):
            return False
        if not super().__eq__(obj):
            return False
        return self.__height == obj.height

    def __hash__(self):
        return hash((super().__hash__(), self.__height))

    def __str__(self):
        return f"TransactionInfo{{ height={self.__height} }} {super().__str__()}"
