from src.registry_structs.registry_key import RegistryKey
from src.features.ifeature import IFeature
from src.registry_structs.registry_value import RegistryValue, ValueType


class EntryName(IFeature):
    def __init__(self, name: str):
        self.name = name

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue("", ValueType.REG_SZ, self.name)
        )
