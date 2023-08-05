from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Literal
from winreg import (
    HKEY_CLASSES_ROOT,
    HKEY_CURRENT_USER,
    HKEY_USERS,
    HKEY_CURRENT_CONFIG,
    HKEY_LOCAL_MACHINE
)


class Location(StrEnum):
    """
    When should the Context Menu be opened? Files? Directories?
    """

    # LEFT_PANEL = r"HKEY_CURRENT_USER\Software\Classes\directory\Background\shell"
    LEFT_PANEL_ADMIN = r"HKEY_CLASSES_ROOT\Directory\Background\shell"

    # RIGHT_PANEL = r"HKEY_CURRENT_USER\Software\Classes\directory\shell"
    RIGHT_PANEL_ADMIN = r"HKEY_CLASSES_ROOT\Directory\shell"

    FILE = r"HKEY_CURRENT_USER\Software\Classes\*\shell"
    FILE_ADMIN = r"HKEY_CLASSES_ROOT\*\shell"

    DESKTOP = r"HKEY_CLASSES_ROOT\DesktopBackground\Shell"


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
