from src.features import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType

NEVER_DEFAULT_VALUE = "NeverDefault"


class NeverDefault(IFeature):
    """
    Tells windows NOT to use this context-menu item in cases where
    there is no known application to open the file extension with.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(NEVER_DEFAULT_VALUE, ValueType.REG_SZ, "")
        )
