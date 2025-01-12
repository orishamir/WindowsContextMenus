from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType

DISABLE_VALUE = "LegacyDisable"


class Disable(IFeature):
    """
    Make the context menu disabled.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(DISABLE_VALUE, ValueType.REG_SZ, "")
        )
