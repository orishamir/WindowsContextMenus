from __future__ import annotations

from dataclasses import dataclass
from typing import Literal
from winreg import (
    HKEY_CLASSES_ROOT,
    HKEY_CURRENT_USER,
    HKEY_USERS,
    HKEY_CURRENT_CONFIG,
    HKEY_LOCAL_MACHINE,
)


@dataclass
class RegistryLocation:
    """
    A convenient way of handling registry locations with `winreg`
    """

    top_level: Literal[
        HKEY_CLASSES_ROOT,
        HKEY_CURRENT_USER,
        HKEY_USERS,
        HKEY_CURRENT_CONFIG,
        HKEY_LOCAL_MACHINE,
    ]
    subkey: str

    def __truediv__(self, other: str) -> RegistryLocation:
        if not isinstance(other, str):
            raise TypeError(f"other must be a string. {type(other)=}")

        return RegistryLocation(
            self.top_level,
            self.subkey.strip("\\") + f"\\{other}"
        )

    def __str__(self) -> str:
        return f"{self.top_level}\\{self.subkey}"
