from __future__ import annotations

import contextlib
import re
import winreg
from enum import IntEnum

from .registry_key import RegistryKey
from .registry_value import DataType, RegistryValue

RESERVED_FLAG = 0


class TopLevelKey(IntEnum):
    """An enum representing the possible top-level registry keys."""

    HKEY_CLASSES_ROOT = winreg.HKEY_CLASSES_ROOT
    HKEY_CURRENT_USER = winreg.HKEY_CURRENT_USER
    HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE
    HKEY_USERS = winreg.HKEY_USERS
    HKEY_CURRENT_CONFIG = winreg.HKEY_CURRENT_CONFIG


_TOP_LEVEL_TO_ENUM: dict[str, TopLevelKey] = {
    "HKEY_CLASSES_ROOT": TopLevelKey.HKEY_CLASSES_ROOT,
    "HKEY_CURRENT_USER": TopLevelKey.HKEY_CURRENT_USER,
    "HKEY_LOCAL_MACHINE": TopLevelKey.HKEY_LOCAL_MACHINE,
    "HKEY_USERS": TopLevelKey.HKEY_USERS,
    "HKEY_CURRENT_CONFIG": TopLevelKey.HKEY_CURRENT_CONFIG,
}


class RegistryPath:
    """Represents a registry location in Windows.

    Provides a convenient interface for interacting with Windows Registry paths.
    This class mimics the API of `pathlib.Path`, allowing intuitive manipulation of registry paths.
    """

    _path: str

    def __init__(self, path: str) -> None:
        """Construct RegistryLocation object from a human-readable location string."""
        normalized_path = self._normalize_raw_path(path)
        self._validate_path(normalized_path)

        self._path = normalized_path

    @property
    def top_level_key(self) -> TopLevelKey:
        r"""The top level key of the path.

        Example:
            ```python
            RegistryPath("HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*").top_level_key
            # ["HKEY_LOCAL_MACHINE", "SOFTWARE", "Classes", "*"]
            ```
        """
        top_level_str, *_ = self._path.split("\\", maxsplit=1)
        return _TOP_LEVEL_TO_ENUM[top_level_str]

    @property
    def subkeys(self) -> str:
        r"""The path without the top level key, i.e. the sub keys.

        Example:
            ```python
            RegistryPath("HKEY_CURRENT_USER\Software\classes\*").subkeys
            # Software\classes\*
            ```
        """
        try:
            _, subkeys = self._path.split("\\", maxsplit=1)
            return subkeys
        except ValueError:
            return ""

    @property
    def parts(self) -> list[str]:
        r"""The path split into parts.

        Example:
            ```python
            RegistryPath("HKEY_CURRENT_USER\Software\classes\*").parts
            # ["HKEY_CURRENT_USER", "Software", "classes", "*"]
            ```
        """
        return self._path.split("\\")

    def read(self) -> RegistryKey:
        """Read key at `self` location, recursively."""
        print("reading at", self)
        tree = RegistryKey(name=self.parts[-1])
        tree.values.extend(self.read_values())

        with (
            winreg.OpenKey(
                self.top_level_key,
                self.subkeys,
                RESERVED_FLAG,
                winreg.KEY_READ,
            ) as key,
            contextlib.suppress(OSError),
        ):
            for i in range(1024):
                subkey_name = winreg.EnumKey(key, i)
                sub_location = self / subkey_name
                tree.add_subkey(sub_location.read())
        return tree

    def read_values(self) -> list[RegistryValue]:
        """Read all values of the key at current location."""
        values: list[RegistryValue] = []

        with (
            winreg.OpenKey(
                self.top_level_key,
                self.subkeys,
                RESERVED_FLAG,
                winreg.KEY_READ,
            ) as key,
            contextlib.suppress(OSError),
        ):
            for i in range(1024):
                name, data, data_type = winreg.EnumValue(key, i)
                values.append(
                    RegistryValue(
                        name=name,
                        type=DataType(data_type),
                        data=data,
                    ),
                )

        return values

    def write(self, key: RegistryKey) -> None:
        """Add RegistryKey to current location."""
        new_loc = self / key.name
        winreg.CloseKey(
            winreg.CreateKey(
                new_loc.top_level_key,
                new_loc.subkeys,
            ),
        )

        for value in key.values:
            new_loc.write_value(value)

        for subkey in key.subkeys:
            new_loc.write(subkey)

    def write_value(self, value: RegistryValue) -> None:
        """Add value to current location."""
        with winreg.OpenKey(
            self.top_level_key,
            self.subkeys,
            RESERVED_FLAG,
            winreg.KEY_WRITE,
        ) as key:
            winreg.SetValueEx(key, value.name, RESERVED_FLAG, value.type, value.data)

    @staticmethod
    def _normalize_raw_path(raw_path: str) -> str:
        r"""Convert raw_path to a normalized registry path string.

        Example:
            ```python
            hkey_current_user\Software/classes\\.mp4/
            ->
            HKEY_CURRENT_USER\Software\classes\.mp4
            ```
        """
        raw_path = raw_path.replace("/", "\\")
        raw_path = re.sub(r"\\+", r"\\", raw_path)
        raw_path = raw_path.strip("\\")

        try:
            top_level, subkeys = raw_path.split("\\", maxsplit=1)
        except ValueError:
            # only top level provided
            return raw_path.upper()

        top_level = top_level.upper()

        return f"{top_level}\\{subkeys}"

    def _validate_path(self, path: str) -> None:
        top_level, *_ = path.split("\\", maxsplit=1)

        if top_level not in _TOP_LEVEL_TO_ENUM:
            raise ValueError(f"top level key does not exist: {top_level}")

    def __truediv__(self, other: object) -> RegistryPath:
        if not isinstance(other, str | RegistryPath):
            return NotImplemented

        if isinstance(other, RegistryPath):
            other = str(other)

        return RegistryPath(
            self._path + f"\\{other.strip('\\')}",
        )

    def __str__(self) -> str:
        try:
            self._validate_path(self._path)
        except ValueError as e:
            # this means something bad happened that caused _path to become invalid.
            raise AssertionError("discrepancy found: internal path is invalid") from e

        return self._path

    def __hash__(self) -> int:
        return hash(self._path)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RegistryPath):
            return NotImplemented

        return self._path == other._path
