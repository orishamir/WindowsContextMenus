from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class MUIVerb(IFeature):
    """Same as EntryName, with small difference.

    This should be used when using sub-menus, instead of EntryName.
    EntryName features inside a ContextMenu will automatically be converted to MUIVerb.
    """
    name: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="MUIVerb", type=DataType.REG_SZ, data=self.name),
        )
