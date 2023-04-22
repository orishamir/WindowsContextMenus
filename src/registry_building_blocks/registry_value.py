from dataclasses import dataclass
from enum import Enum
from typing import Any


class ValueType(Enum):
    pass


@dataclass
class RegistryValue:
    """
    Represents a Registry Value as defined in https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry
    """

    name: str
    type: ValueType
    data: Any
