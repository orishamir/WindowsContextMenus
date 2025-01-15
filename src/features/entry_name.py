from dataclasses import dataclass

from src.features.ifeature import IFeature
from src.registry_structs.registry_key import RegistryKey
from src.registry_structs.registry_value import RegistryValue, DataType

DEFAULT_VALUE = ""


@dataclass
class EntryName(IFeature):
    """
    This feature defines what text shows up
    in the actual context menu, i.e. the
    text that appears after right-click
    """

    name: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=DEFAULT_VALUE, type=DataType.REG_SZ, data=self.name)
        )
