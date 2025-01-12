import winreg
from dataclasses import dataclass
from enum import IntEnum
from typing import Any


class ValueType(IntEnum):
    """
    Some constant value types as defined in
    https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types
    """

    REG_BINARY = winreg.REG_BINARY
    REG_DWORD = winreg.REG_DWORD
    REG_SZ = winreg.REG_SZ


@dataclass
class RegistryValue:
    """
    Represents a registry value as defined in
    https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry
    """

    name: str
    type: ValueType
    data: Any
