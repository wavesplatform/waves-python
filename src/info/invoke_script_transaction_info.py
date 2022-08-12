from src.info.transaction_info import TransactionInfo
from src.model.application_status import ApplicationStatus
from src.transaction.invoke_script_transaction import InvokeScriptTransaction


class InvokeScriptTransactionInfo(TransactionInfo):

    def __init__(self, tx: InvokeScriptTransaction, application_status: ApplicationStatus, height: int, state_changes: StateChanges) -> None:
        self.__state_changes = state_changes
        super().__init__(tx, application_status, height)

    @property
    def tx(self):
        return super().tx

    @property
    def state_changes(self):
        return self.__state_changes

    def __eq__(self, obj):
        if self == obj:
            return True
        if obj is None or not isinstance(obj, self.__class__):
            return False
        if not super().__eq__(obj):
            return False
        return self.__state_changes == obj.state_changes

    def __hash__(self):
        return hash((super().__hash__(), self.__state_changes))

    def __str__(self):
        return f"InvokeScriptTransactionInfo{{ state_changes={self.__state_changes} }} {super().__str__()}"
