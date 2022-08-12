from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.reissue_transaction import ReissueTransaction


class ReissueTransactionInfo(TransactionInfo):

    def __init__(self, tx: ReissueTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"ReissueTransactionInfo{{}} {super().__str__()}"
