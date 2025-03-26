from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class ShiftClick(IShellAttribute):
    """Open context menu only when shift is pressed alongside right click."""

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="Extended", type=DataType.REG_SZ, data=""),
        )
