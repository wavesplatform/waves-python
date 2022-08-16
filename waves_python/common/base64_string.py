from waves_python.common.ByteString import ByteString


class Base64String(ByteString):

    def __init__(self, base64_encoded=None, byte_array=None) -> None:
        self.__byte_array = bytearray() if not byte_array else byte_array
        self.__encoded = base64_encoded

    @classmethod
    def empty(cls):
        public_key = cls()
        return public_key

    def byte_array(self) -> bytearray:
        return self.__byte_array

    def encoded(self) -> str:
        return self.__encoded

    def encoded_with_prefix(self) -> str:
        return f"base64:{self.__encoded}"
