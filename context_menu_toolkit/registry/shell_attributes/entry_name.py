from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

DEFAULT_VALUE = ""


@dataclass
class EntryName(IShellAttribute):
    """Fallback method of specifying display text of the context menu."""

    text: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=DEFAULT_VALUE, type=DataType.REG_SZ, data=self.text),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "EntryName | None":
        value = tree.get_value(DEFAULT_VALUE)
        if value is not None and isinstance(value.data, str):
            return EntryName(value.data)
        return None
