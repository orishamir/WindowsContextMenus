"""
Source:
    https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#creating-cascading-menus-with-the-extendedsubcommandskey-registry-entry
"""
from dataclasses import dataclass
from enum import IntEnum

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class Separator(IFeature):
    """
    Adds a line separator before or after the context menu.
    For looks.
    Only works with submenus.
    """
    class Location(IntEnum):
        Before = 0x20  # ECF_SEPARATORBEFORE
        After = 0x40  # ECF_SEPARATORAFTER

    location: Location

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="CommandFlags", type=DataType.REG_DWORD, data=self.location),
        )
