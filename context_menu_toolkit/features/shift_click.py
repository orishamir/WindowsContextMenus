from dataclasses import dataclass

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import RegistryKey, RegistryValue, DataType

SHIFT_CLICK_VALUE = "Extended"


@dataclass
class ShiftClick(IFeature):
    """
    Open context menu only when shift is pressed as well.
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=SHIFT_CLICK_VALUE, type=DataType.REG_SZ, data="")
        )
