from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.sponsor_fee_transaction import SponsorFeeTransaction


class SponsorFeeTransactionInfo(TransactionInfo):

    def __init__(self, tx: SponsorFeeTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"SponsorFeeTransactionInfo{{}} {super().__str__()}"
