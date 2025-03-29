from dataclasses import dataclass
from enum import IntEnum
from typing import Literal

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "CommandFlags"


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
        data = SeperatorLocation.After if self.location == "After" else SeperatorLocation.Before
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_DWORD, data=data),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "Separator | None":
        value = tree.get_value(ATTRIBUTE_NAME)
        if value is not None and isinstance(value.data, str):
            return Separator(
                "After" if value.data == SeperatorLocation.After else "Before",
            )
        return None


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
