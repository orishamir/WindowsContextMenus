from dataclasses import dataclass

from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType

NEVER_DEFAULT_VALUE = "NeverDefault"


@dataclass
class NeverDefault(IFeature):
    """
    Tells windows NOT to use this context-menu item in cases where
    there is no known application to open the file extension with.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=NEVER_DEFAULT_VALUE, type=DataType.REG_SZ, data="")
        )
