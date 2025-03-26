from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class Note(IShellAttribute):
    """Add a note in the registry (does not affect functionality).

    Attributes:
        note: The text note that should be added to the registry.
    """
    note: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="Note", type=DataType.REG_SZ, data=self.note),
        )
