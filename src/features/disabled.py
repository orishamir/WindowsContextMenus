from dataclasses import dataclass

from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType

DISABLE_VALUE = "LegacyDisable"


@dataclass
class Disabled(IFeature):
    """
    Make the context menu disabled.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=DISABLE_VALUE, type=DataType.REG_SZ, data="")
        )
