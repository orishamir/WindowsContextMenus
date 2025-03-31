from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "Extended"


@dataclass
class ShiftClick(IShellAttribute):
    """Open context menu only when shift is pressed alongside right click."""

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=""),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "ShiftClick | None":
        if tree.contains_value(ATTRIBUTE_NAME):
            return ShiftClick()
        return None
