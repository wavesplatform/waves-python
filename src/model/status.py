from enum import Enum


class Status(Enum):
    NOT_FOUND = "not_found"
    UNCONFIRMED = "unconfirmed"
    CONFIRMED = "confirmed"
