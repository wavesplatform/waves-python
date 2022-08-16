from dataclasses import dataclass


@dataclass
class Alias:
    name: str
    chainId: int = 87
