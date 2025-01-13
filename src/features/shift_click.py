from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType

SHIFT_CLICK_VALUE = "Extended"


class ShiftClick(IFeature):
    """
    Open context menu only when shift is pressed as well.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(SHIFT_CLICK_VALUE, DataType.REG_SZ, "")
        )
