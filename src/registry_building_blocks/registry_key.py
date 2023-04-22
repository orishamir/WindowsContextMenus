from __future__ import annotations

from dataclasses import dataclass

from src.registry_building_blocks.registry_value import RegistryValue


@dataclass
class RegistryKey:
    values: list[RegistryValue]
    subkeys: list[RegistryKey]
