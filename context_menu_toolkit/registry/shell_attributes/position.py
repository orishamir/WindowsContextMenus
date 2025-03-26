from dataclasses import dataclass
from typing import Literal

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class Position(IShellAttribute):
    """Determines the general position of the context menu.

    Attributes:
        position: "Top" or "Bottom".

    Warning:
        This attribute will NOT necessarily set the position.
        The way Windows determines the location is complicated,
        and Position attribute merely specifies the general preference.
        For example, it may move your context menu lower down the list, but not all the way.
    """
    position: Literal["Top", "Bottom"]

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="Position", type=DataType.REG_SZ, data=self.position),
        )
