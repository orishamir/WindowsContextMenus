from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import RegistryKey, RegistryValue, DataType


@dataclass
class Disabled(IFeature):
    """
    Make the context menu disabled.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="LegacyDisable", type=DataType.REG_SZ, data="")
        )
