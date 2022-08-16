from waves_python.common.base58_string import Base58String
from waves_python.common.crypto import Crypto


class PrivateKey(Base58String):
    LENGTH = 32

    def __init__(self, base58_encoded: str = None, byte_array: bytearray = None) -> None:
        if base58_encoded and byte_array:
            raise Exception()
        super().__init__(base58_encoded, byte_array)

    @classmethod
    def from_seed(cls, seed_phrase: str = None, seed_phrase_bytes: bytearray = None, nonce: int = None):
        public_key = cls(base58_encoded=Crypto.get_private_key(Crypto.get_account_seed(seed_phrase_bytes, nonce)))
        return public_key

    @classmethod
    def from_str(cls, base58_encoded: str):
        public_key = cls(base58_encoded=base58_encoded)
        return public_key

    @classmethod
    def from_bytes(cls, byte_array: bytearray):
        public_key = cls(byte_array=byte_array)
        return public_key

    def is_signature_valid(self, message: bytearray, signature: bytearray):
        if len(signature) != 64:
            raise ValueError(f"Signature has wrong size in bytes. Expected: 64, actual: {len(signature)}")
        else:
            return Crypto.is_proof_valid(self.byte_array, message, signature)

    def __eq__(self, obj):
        if self == obj:
            return True
        elif obj and not isinstance(obj, self.__class__):
            return self.byte_array == obj.byte_array
        else:
            return False

    def __hash__(self):
        return hash((super().__hash__(), self.byte_array))

    def __str__(self):
        return self.encoded()