from src.model.application_status import ApplicationStatus
from src.transaction.transaction import Transaction


class TransactionWithStatus:

    def __init__(self, tx: Transaction, application_status: ApplicationStatus) -> None:
        super().__init__(tx, application_status)
        self.__tx = tx
        self.__application_status = application_status

    @property
    def tx(self) -> Transaction:
        return self.__tx

    @property
    def application_status(self) -> ApplicationStatus:
        return self.__application_status

    def __eq__(self, obj):
        if self == obj:
            return True
        if obj is None or not isinstance(obj, self.__class__):
            return False
        return self.__tx == obj.__tx and self.__application_status == obj.__application_status

    def __hash__(self):
        return hash((self.__tx, self.__application_status))

    def __str__(self):
        return f"TransactionWithStatus{{ tx={self.__tx}, application_status={self.__application_status} }}"
