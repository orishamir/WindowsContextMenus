from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "Icon"


@dataclass
class Icon(IShellAttribute):
    """Add an icon that will be displayed for the context menu.

    Attributes:
        icon_path: Windows dll/exe icon, or a path on the local machine for the icon.
    """

    icon_path: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=self.icon_path),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "Icon | None":
        value = tree.get_value(ATTRIBUTE_NAME)
        if value is not None and isinstance(value.data, str):
            return Icon(value.data)
        return None
