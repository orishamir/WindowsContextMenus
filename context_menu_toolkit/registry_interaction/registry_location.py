from __future__ import annotations

import winreg
from enum import IntEnum

from pydantic import BaseModel


class _TopLevelKey(IntEnum):
    HKEY_CLASSES_ROOT = winreg.HKEY_CLASSES_ROOT
    HKEY_CURRENT_USER = winreg.HKEY_CURRENT_USER
    HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE
    HKEY_USERS = winreg.HKEY_USERS
    HKEY_CURRENT_CONFIG = winreg.HKEY_CURRENT_CONFIG


_TOP_LEVEL_STR_TO_HKEY: dict[str, _TopLevelKey] = {
    "HKEY_CLASSES_ROOT": _TopLevelKey.HKEY_CLASSES_ROOT,
    "HKEY_CURRENT_USER": _TopLevelKey.HKEY_CURRENT_USER,
    "HKEY_LOCAL_MACHINE": _TopLevelKey.HKEY_LOCAL_MACHINE,
    "HKEY_USERS": _TopLevelKey.HKEY_USERS,
    "HKEY_CURRENT_CONFIG": _TopLevelKey.HKEY_CURRENT_CONFIG,
}


class _RegistryLocation(BaseModel):
    """Represents a registry location in Windows.

    Providing a convenient interface for interacting
    with the Windows Registry.
    This class mimics the API of `pathlib.Path`, allowing intuitive manipulation of registry paths.
    """

    top_level: _TopLevelKey
    subkey: str

    def __truediv__(self, other: str) -> _RegistryLocation:
        if not isinstance(other, str):
            raise TypeError(f"other must be a string. {type(other)=}")

        return _RegistryLocation(
            top_level=self.top_level,
            subkey=self.subkey.strip("\\") + f"\\{other}",
        )

    def __str__(self) -> str:
        r"""Representation of a registry location as a string.

        Example:
            > RegistryLocation.from_string(
            >     "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell",
            > )
            # output: "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell"
        """
        return f"{self.top_level.name}\\{self.subkey}"

    @classmethod
    def from_string(cls, location: str) -> _RegistryLocation:
        r"""Construct RegistryLocation object from a human-readable location string.

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

        if top_level not in _TOP_LEVEL_STR_TO_HKEY:
            raise ValueError(f"invalid top level key: {top_level}")

        return _RegistryLocation(
            top_level=_TOP_LEVEL_STR_TO_HKEY[top_level],
            subkey=subkey,
        )
