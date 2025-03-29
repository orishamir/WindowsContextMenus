from dataclasses import dataclass

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "AppliesTo"


@dataclass
class AppliesTo(IShellAttribute):
    """Add an Advanced Query Syntax condition."""
    aqs_condition: str

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=self.aqs_condition),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "AppliesTo | None":
        value = tree.get_value(ATTRIBUTE_NAME)
        if value is not None and isinstance(value.data, str):
            return AppliesTo(value.data)
        return None
