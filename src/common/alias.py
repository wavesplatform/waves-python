class Alias:

    PREFIX = "alias:"
    TYPE = 2
    MIN_LENGTH = 4
    MAX_LENGTH = 30
    BYTES_LENGTH = 32
    ALPHABET = "-.0-9@_a-z"

    def __init__(self, name: str, chain_id: bytes = None) -> None:
        self.chain_id = chain_id
        if not self.__is_valid(chain_id, name):
            raise Exception()
        self.name = name
        self.full_alias = full_alias
