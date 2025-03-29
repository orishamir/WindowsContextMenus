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
        top_level_str, _ = self._path.split("\\", maxsplit=1)
        return TopLevelKey(top_level_str)

    @property
    def subkeys(self) -> str:
        r"""The path without the top level key, i.e. the sub keys.

        Example:
            ```python
            RegistryPath("HKEY_CURRENT_USER\Software\classes\*").subkeys
            # Software\classes\*
            ```
        """
        _, subkeys = self._path.split("\\", maxsplit=1)
        return subkeys

    @property
    def parts(self) -> list[str]:
        r"""The path split into parts.

        Example:
            ```python
            RegistryPath("HKEY_CURRENT_USER\Software\classes\*").parts
            # Software\classes\*
            ```
        """
        return self._path.split("\\")

    @staticmethod
    def _normalize_raw_path(raw_path: str) -> str:
        r"""Convert raw_path to a normalized registry path string.

        Example:
            ```
            hkey_current_user\Software/classes\\.mp4/
            ->
            HKEY_CURRENT_USER\Software\classes\.mp4
            ```
        """
        raw_path = raw_path.replace("/", "\\")
        raw_path = re.sub(r"\\+", r"\\", raw_path)
        raw_path = raw_path.strip("\\")

        top_level, subkeys = raw_path.split("\\", maxsplit=1)
        top_level = top_level.upper()

        return f"{top_level}\\{subkeys}"

    def _validate_path(self, path: str) -> None:
        top_level, _ = path.split("\\", maxsplit=1)

        if top_level not in TopLevelKey:
            raise ValueError(f"top level key does not exist: {top_level}")

    def __truediv__(self, other: str | RegistryPath) -> RegistryPath:
        assert isinstance(other, str | RegistryPath), f"other must be a string or RegistryPath. {type(other)=}"

        if isinstance(other, RegistryPath):
            other = str(other)

        return RegistryPath(
            self._path + f"\\{other.strip('\\')}",
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
