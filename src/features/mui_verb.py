from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType


class MUIVerb(IFeature):
    """
    Same as EntryName, but this should be used when
    using sub-menus as well.
    EntryName features inside a ContextMenu will
    automatically be converted to MUIVerb.
    """

    def __init__(self, name: str):
        self.name = name

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue("MUIVerb", ValueType.REG_SZ, self.name)
        )
