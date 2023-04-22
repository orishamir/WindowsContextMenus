from __future__ import annotations

from dataclasses import dataclass

from src.registry_building_blocks.registry_value import RegistryValue


@dataclass
class RegistryKey:
    """
    Represents a Registry Key as defined in https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry
    """

    values: list[RegistryValue]
    subkeys: list[RegistryKey]
