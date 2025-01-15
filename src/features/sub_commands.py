from dataclasses import dataclass

from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType


@dataclass
class SubCommands(IFeature):
    """
    A ContextMenu with submenus needs to have
    this feature, and will automatically be added
    if the ContextMenu instance has submenus.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="SubCommands", type=DataType.REG_SZ, data="")
        )
