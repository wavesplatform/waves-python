class ByteString:

    def byte_array(self) -> bytearray:
        raise NotImplementedError()

    def encoded(self) -> str:
        raise NotImplementedError()

    def encoded_with_prefix(self) -> str:
        raise NotImplementedError()
