from enum import Enum


class Profile(Enum):
    MAINNET = "https://nodes.wavesnodes.com"
    STAGENET = "https://nodes-stagenet.wavesnodes.com"
    TESTNET = "https://nodes-testnet.wavesnodes.com"
    LOCAL = "http://127.0.0.1:8081"
