from __future__ import annotations

from dataclasses import dataclass, field

from src.registry_structs.registry_value import RegistryValue


@dataclass
class RegistryKey:
    name: str
    values: list[RegistryValue] = field(default_factory=list)
    subkeys: list[RegistryKey] = field(default_factory=list)
