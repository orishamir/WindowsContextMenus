from __future__ import annotations

import winreg
from dataclasses import dataclass
from enum import IntEnum


class TopLevelKey(IntEnum):
    HKEY_CLASSES_ROOT = winreg.HKEY_CLASSES_ROOT
    HKEY_CURRENT_USER = winreg.HKEY_CURRENT_USER
    HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE
    HKEY_USERS = winreg.HKEY_USERS
    HKEY_CURRENT_CONFIG = winreg.HKEY_CURRENT_CONFIG


TOP_LEVEL_STR_TO_HKEY: dict[str, TopLevelKey] = {
    "HKEY_CLASSES_ROOT": TopLevelKey.HKEY_CLASSES_ROOT,
    "HKEY_CURRENT_USER": TopLevelKey.HKEY_CURRENT_USER,
    "HKEY_LOCAL_MACHINE": TopLevelKey.HKEY_LOCAL_MACHINE,
    "HKEY_USERS": TopLevelKey.HKEY_USERS,
    "HKEY_CURRENT_CONFIG": TopLevelKey.HKEY_CURRENT_CONFIG,
}


@dataclass
class _RegistryLocation:
    """
    A convenient way of handling registry locations with `winreg`
    """

    top_level: TopLevelKey
    subkey: str

    def __truediv__(self, other: str) -> _RegistryLocation:
        if not isinstance(other, str):
            raise TypeError(f"other must be a string. {type(other)=}")

        return _RegistryLocation(
            self.top_level,
            self.subkey.strip("\\") + f"\\{other}",
        )

    def __str__(self) -> str:
        r"""
        Example:
            > RegistryLocation.from_string(
            >     "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell",
            > )
            # output: "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell"
        """
        return f"{self.top_level.name}\\{self.subkey}"

    @classmethod
    def from_string(cls, location: str) -> _RegistryLocation:
        r"""
        Construct RegistryLocation object from a human-readable location string.
        Example:
            > print(repr(RegistryLocation.from_string(
            >     "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell",
            > )))
            # output:
            # RegistryLocation(
            #     top_level=TopLevelKey.HKEY_LOCAL_MACHINE,
            #     subkey="SOFTWARE\Classes\*\shell\ConvertVideo\shell",
            # )
        """
        top_level, subkey = location.split("\\", maxsplit=1)

        if top_level not in TOP_LEVEL_STR_TO_HKEY:
            raise ValueError(f"invalid top level key: {top_level}")

        return _RegistryLocation(
            TOP_LEVEL_STR_TO_HKEY[top_level],
            subkey,
        )
