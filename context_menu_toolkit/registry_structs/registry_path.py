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

    _normalized_path: str

    def __init__(self, *args: str) -> None:
        """Construct RegistryLocation object from a human-readable location string."""
        path = "\\".join(args)

        normalized_path = self._normalize_raw_path(path)
        self._validate_path(normalized_path)

        self._normalized_path = normalized_path

    @property
    def top_level_key(self) -> TopLevelKey:
        r"""The top level key of the path.

        Example:
            ```python
            RegistryPath("HKEY_CURRENT_USER\Software\classes\*").top_level_key
            # TopLevelKey.HKEY_CURRENT_USER
            ```
        """
        top_level_str, _ = self._normalized_path.split("\\", maxsplit=1)
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
        _, subkeys = self._normalized_path.split("\\", maxsplit=1)
        return subkeys

    @property
    def parent(self) -> RegistryPath:
        parts = self.parts
        if len(parts) == 1:
            return self

        return RegistryPath(*parts[:-1])

    @property
    def parts(self) -> list[str]:
        return self._normalized_path.split("\\")

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
            self._normalized_path + f"\\{other.strip("\\")}",
        )

    def __str__(self) -> str:
        r"""Representation of a registry location as a string.

        Example:
            > RegistryLocation.from_string(
            >     "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell",
            > )
            # output: "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\ConvertVideo\shell"
        """
        return self._normalized_path

    def __hash__(self) -> int:
        return hash(self._normalized_path)

    def __eq__(self, other: object) -> bool:
        return str(self) == str(other)

