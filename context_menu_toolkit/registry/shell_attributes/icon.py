from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class Icon(IShellAttribute):
    """Add an icon that will be displayed for the context menu.

    Attributes:
        icon_path: Windows dll/exe icon, or a path on the local machine for the icon.
    """
    icon_path: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="Icon", type=DataType.REG_SZ, data=self.icon_path),
        )
