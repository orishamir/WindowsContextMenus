from src.features.ifeature import IFeature
from src.registry_structs.registry_key import RegistryKey
from src.registry_structs.registry_value import RegistryValue, DataType

DEFAULT_VALUE = ""


class EntryName(IFeature):
    """
    This feature defines what text shows up
    in the actual context menu, i.e. the
    text that appears after right-click
    """

    def __init__(self, name: str):
        self.name = name

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(DEFAULT_VALUE, DataType.REG_SZ, self.name)
        )
