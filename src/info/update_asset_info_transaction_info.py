from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.update_asset_info_transaction import UpdateAssetInfoTransaction


class UpdateAssetInfoTransactionInfo(TransactionInfo):

    def __init__(self, tx: UpdateAssetInfoTransaction, application_status: ApplicationStatus, height: int) -> None:
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    def __str__(self):
        return f"UpdateAssetInfoTransactionInfo{{}} {super().__str__()}"
