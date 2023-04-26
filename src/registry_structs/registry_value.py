import winreg
from dataclasses import dataclass
from enum import EnumMeta
from typing import Any


class ValueType(EnumMeta):
    REG_BINARY = winreg.REG_BINARY
    REG_DWORD = winreg.REG_DWORD
    REG_SZ = winreg.REG_SZ


@dataclass
class RegistryValue:
    name: str
    type: ValueType
    data: Any
