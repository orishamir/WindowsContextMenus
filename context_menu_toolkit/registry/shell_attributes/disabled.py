from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class Disabled(IShellAttribute):
    """Make the context menu disabled."""

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="LegacyDisable", type=DataType.REG_SZ, data=""),
        )
