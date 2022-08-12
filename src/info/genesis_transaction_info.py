from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.genesis_transaction import GenesisTransaction


class GenesisTransactionInfo(TransactionInfo):

    def __init__(self, tx: GenesisTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"GenesisTransactionInfo{{}} {super().__str__()}"
