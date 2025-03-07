from __future__ import annotations

import re
from enum import StrEnum


class TopLevelKey(StrEnum):
    """An enum representing the possible top-level registry keys."""
    HKEY_CLASSES_ROOT = "HKEY_CLASSES_ROOT"
    HKEY_CURRENT_USER = "HKEY_CURRENT_USER"
    HKEY_LOCAL_MACHINE = "HKEY_LOCAL_MACHINE"
    HKEY_USERS = "HKEY_USERS"
    HKEY_CURRENT_CONFIG = "HKEY_CURRENT_CONFIG"


class RegistryPath:
    """Represents a registry location in Windows.

    Providing a convenient interface for interacting
    with the Windows Registry.
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
        top_level_str, _ = self._path.split("\\", maxsplit=1)
        return TopLevelKey(top_level_str)

    @property
    def subkeys(self) -> str:
        _, subkeys = self._path.split("\\", maxsplit=1)
        return subkeys

    def _normalize_raw_path(self, raw_path: str) -> str:
        r"""Convert raw_path to a normalized registry path string.

        Example:
            ```
            hkey_local_user\Software/classes\\.mp4/
            ->
            HKEY_LOCAL_USER\Software\classes\.mp4
            ```
        """
        raw_path = raw_path.replace("/", "\\")
        raw_path = re.sub(r"\\+", r"\\", raw_path).strip("\\")

        top_level, subkeys = raw_path.split("\\", maxsplit=1)
        top_level = top_level.upper()

        return f"{top_level}\\{subkeys}"

    def _validate_path(self, path: str) -> None:
        top_level, subkeys = path.split("\\", maxsplit=1)

        if top_level not in TopLevelKey:
            raise ValueError(f"top level key does not exist: {top_level}")

    def __truediv__(self, other: str | RegistryPath) -> RegistryPath:
        if not isinstance(other, str | RegistryPath):
            raise TypeError(f"other must be a string or RegistryPath. {type(other)=}")

        if isinstance(other, RegistryPath):
            other = str(other)

        return RegistryPath(
            self._path + f"\\{other.strip("\\")}",
        )

    def __str__(self) -> str:
        r"""Representation of a registry location as a string.

        Example:
            > RegistryLocation.from_string(
            >     "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell",
            > )
            # output: "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell"
        """
        try:
            self._validate_path(self._path)
        except ValueError as e:
            # this means something bad happened that caused _path to become invalid.
            raise AssertionError("discrepancy found: internal path is invalid") from e

        return self._path
