from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class Note(IFeature):
    """Add a note in the registry (does not affect functionality).

    Attributes:
        note: The text note that should be added to the registry.
    """

    note: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="Note", type=DataType.REG_SZ, data=self.note),
        )
