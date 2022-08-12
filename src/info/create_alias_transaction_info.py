from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.create_alias_transaction import CreateAliasTransaction


class CreateAliasTransactionInfo(TransactionInfo):

    def __init__(self, tx: CreateAliasTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"CreateAliasTransactionInfo{{}} {super().__str__()}"
