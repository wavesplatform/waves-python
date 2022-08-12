from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.lease_cancel_transaction import LeaseCancelTransaction


class LeaseCancelTransactionInfo(TransactionInfo):

    def __init__(self, tx: LeaseCancelTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"LeaseCancelTransactionInfo{{}} {super().__str__()}"
