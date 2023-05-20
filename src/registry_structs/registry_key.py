from __future__ import annotations

from dataclasses import dataclass, field

from src.registry_structs.registry_value import RegistryValue


@dataclass
class RegistryKey:
    """
    This dataclass represents a registry key as defined in https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry
    """

    name: str
    values: list[RegistryValue] = field(default_factory=list)
    subkeys: list[RegistryKey] = field(default_factory=list)
