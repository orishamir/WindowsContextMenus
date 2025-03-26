from dataclasses import dataclass
from typing import Literal

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class Separator(IShellAttribute):
    """Adds a line separator before or after the context menu.

    Attributes:
        location: Where the separator should be, relative to the containing context menu.

    Warning:
        This will most probably work if the context menu is a submenu,
        but is not guaranteed to work with normal menu.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#creating-cascading-menus-with-the-extendedsubcommandskey-registry-entry>
    """

    location: Literal["After", "Before"]

    def apply_to_tree(self, tree: RegistryKey) -> None:
        # ECF_SEPARATORAFTER, ECF_SEPARATORBEFORE
        data = 0x40 if self.location == "After" else 0x20
        tree.add_value(
            RegistryValue(name="CommandFlags", type=DataType.REG_DWORD, data=data),
        )
