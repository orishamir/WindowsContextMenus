from dataclasses import dataclass
from enum import Enum
from typing import Any


class ValueType(Enum):
    pass


@dataclass
class RegistryValue:
    name: str
    type: ValueType
    data: Any
