from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.set_asset_script_transaction import SetAssetScriptTransaction


class SetAssetScriptTransactionInfo(TransactionInfo):

    def __init__(self, tx: SetAssetScriptTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"SetAssetScriptTransactionInfo{{}} {super().__str__()}"
