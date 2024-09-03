from enum import Enum, unique


@unique
class Formatting(Enum):
    DATETIME = "%Y/%m/%d %H:%M:%S"
