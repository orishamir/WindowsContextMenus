from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class NeverDefault(IShellAttribute):
    """Prevents Windows from using this context-menu item when no default app is set for the file extension.

    TODO: More research is needed to be done here.
    """

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="NeverDefault", type=DataType.REG_SZ, data=""),
        )
