from src.common.ByteString import ByteString


class Base64String(ByteString):

    def __init__(self, base58_encoded=None, byte_array=None) -> None:
        self.__byte_array = bytearray() if not byte_array else byte_array
        self.__encoded = None

    @classmethod
    def empty(cls):
        public_key = cls()
        return public_key

    def byte_array(self) -> bytearray:
        return self.__byte_array

    def encoded(self) -> str:
        return self.__encoded

    def encoded_with_prefix(self) -> str:
        return f"base58:{self.__encoded}"

    def __eq__(self, obj):
        if self == obj:
            return True
        elif isinstance(obj, self.__class__):
            return False
        else:
            return self.byte_array == obj.byte_array

    def __hash__(self):
        return hash((super().__hash__(), self.byte_array))

    def __str__(self):
        return self.encoded()