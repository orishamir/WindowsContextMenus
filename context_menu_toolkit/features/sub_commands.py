from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class SubCommands(IFeature):
    """Feature that enables a ContextMenu to have subcommands.

    A ContextMenu with submenus needs to have this feature, and will automatically
    be added when instantiating a ContextMenu with subcommands.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="SubCommands", type=DataType.REG_SZ, data=""),
        )
