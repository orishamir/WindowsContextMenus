from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class Disabled(IFeature):
    """Make the context menu disabled."""

    def apply_registry(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="LegacyDisable", type=DataType.REG_SZ, data=""),
        )
