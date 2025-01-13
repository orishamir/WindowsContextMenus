from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType


class SubCommands(IFeature):
    """
    A ContextMenu with submenus needs to have
    this feature, and will automatically be added
    if the ContextMenu instance has submenus.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue("SubCommands", DataType.REG_SZ, "")
        )
