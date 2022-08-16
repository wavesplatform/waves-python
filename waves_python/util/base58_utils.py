import base58

from waves_python.common.base58_string import Base58String


def from_string(wif: str):
    return base58.b58decode(wif)


def to_string(decoded: str):
    return base58.b58encode(decoded).decode("utf-8")


def base58_to_string(decoded: Base58String):
    return base58.b58encode(decoded.__str__()).decode("utf-8")

