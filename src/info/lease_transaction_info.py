from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.lease_transaction import LeaseTransaction


class LeaseTransactionInfo(TransactionInfo):

    def __init__(self, tx: LeaseTransaction, application_status: ApplicationStatus, height: int, lease_status: LeaseStatus) -> None:
        self.__status = lease_status
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    @property
    def status(self):
        return self.__status

    def __eq__(self, obj):
        if self == obj:
            return True
        if obj is None or not isinstance(obj, self.__class__):
            return False
        if not super().__eq__(obj):
            return False
        return self.__status == obj.status

    def __hash__(self):
        return hash((super().__hash__(), self.__status))

    def __str__(self):
        return f"LeaseTransactionInfo{{ stateChanges={self.__status} }} {super().__str__()}"
