from dataclasses import dataclass

from windows_context_menus.registry.registry_structs import DataType, RegistryKey, RegistryValue
from windows_context_menus.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "NeverDefault"


@dataclass
class NeverDefault(IShellAttribute):
    """Prevents Windows from using this context-menu item when no default app is set for the file extension.

    TODO: More research is needed to be done here.
    """

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=""),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "NeverDefault | None":
        if tree.contains_value(ATTRIBUTE_NAME):
            return NeverDefault()
        return None
