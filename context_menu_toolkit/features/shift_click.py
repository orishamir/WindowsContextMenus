from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class ShiftClick(IFeature):
    """Open context menu only when shift is pressed alongside right click."""

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="Extended", type=DataType.REG_SZ, data=""),
        )
