from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "Note"


@dataclass
class Note(IShellAttribute):
    """Add a note in the registry (does not affect functionality).

    Attributes:
        note: The text note that should be added to the registry.
    """

    note: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=self.note),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "Note | None":
        value = tree.get_value(ATTRIBUTE_NAME)
        if value is not None and isinstance(value.data, str):
            return Note(value.data)
        return None
