from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType


class MUIVerb(IFeature):
    def __init__(self, name: str):
        self.name = name

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue("MUIVerb", ValueType.REG_SZ, self.name)
        )
