from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType


class SubCommands(IFeature):
    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue("SubCommands", ValueType.REG_SZ, "")
        )
