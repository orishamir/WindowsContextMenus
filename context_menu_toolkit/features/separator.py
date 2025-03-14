from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class Separator(IFeature):
    """Adds a line separator before or after the context menu.

    Only works with submenus.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#creating-cascading-menus-with-the-extendedsubcommandskey-registry-entry>
    """

    location: SeperatorLocation

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="CommandFlags", type=DataType.REG_DWORD, data=self.location),
        )


class SeperatorLocation(IntEnum):
    """Where the separator should be, relative to the containing context menu.

    Warning:
        This will most probably work if the context menu is a submenu,
        but is not guaranteed to work with normal menu.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#creating-cascading-menus-with-the-extendedsubcommandskey-registry-entry>
    """
    Before = 0x20  # ECF_SEPARATORBEFORE
    After = 0x40  # ECF_SEPARATORAFTER
