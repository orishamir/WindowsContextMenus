from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class NeverDefault(IFeature):
    """Prevents Windows from using this context-menu item when no default app is set for the file extension.

    TODO: More research is needed to be done here.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="NeverDefault", type=DataType.REG_SZ, data=""),
        )
