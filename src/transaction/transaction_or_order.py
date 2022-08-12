class TransactionOrOrder:

    def __init__(self) -> None:
        self.id = None
        self.version = None
        self.chainId = None
        self.sender = None
        self.fee = None
        self.timestamp = None
        self.proofs = None
        self.bodyBytes = None
