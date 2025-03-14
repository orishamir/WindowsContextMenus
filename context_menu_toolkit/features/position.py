from dataclasses import dataclass
from typing import Literal

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class Position(IFeature):
    """Determines the general position of the context menu.

    Attributes:
        position: "Top" or "Bottom".

    Warning:
        This feature will NOT necessarily set the position.
        The way Windows determines the location is complicated,
        and Position feature merely specifies the general preference.
        For example, it may move your context menu lower down the list, but not all the way.
    """
    position: Literal["Top", "Bottom"]

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="Position", type=DataType.REG_SZ, data=self.position),
        )
