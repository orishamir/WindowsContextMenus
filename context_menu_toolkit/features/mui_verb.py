from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import RegistryKey, RegistryValue, DataType


@dataclass
class MUIVerb(IFeature):
    """
    Same as EntryName, but this should be used when
    using sub-menus as well.
    EntryName features inside a ContextMenu will
    automatically be converted to MUIVerb.
    """
    name: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="MUIVerb", type=DataType.REG_SZ, data=self.name)
        )
