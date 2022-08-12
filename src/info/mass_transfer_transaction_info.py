from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.mass_transfer_transaction import MassTransferTransaction


class MassTransferTransactionInfo(TransactionInfo):

    def __init__(self, tx: MassTransferTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"MassTransferTransactionInfo{{}} {super().__str__()}"
