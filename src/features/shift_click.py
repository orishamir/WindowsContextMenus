from src.features import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType

SHIFT_CLICK_VALUE = "Extended"


class ShiftClick(IFeature):
    """
    Open context menu only when shift is pressed as well.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(SHIFT_CLICK_VALUE, ValueType.REG_SZ, "")
        )
