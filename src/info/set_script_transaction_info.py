from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.set_script_transaction import SetScriptTransaction


class SetScriptTransactionInfo(TransactionInfo):

    def __init__(self, tx: SetScriptTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"SetScriptTransactionInfo{{}} {super().__str__()}"
