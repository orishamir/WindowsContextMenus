from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class NeverDefault(IFeature):
    """Tells windows NOT to use this context-menu item in cases where
    there is no known application to open the file extension with.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="NeverDefault", type=DataType.REG_SZ, data=""),
        )
