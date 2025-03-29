from dataclasses import dataclass
from typing import Literal

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute

ATTRIBUTE_NAME = "Position"


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
            RegistryValue(name=ATTRIBUTE_NAME, type=DataType.REG_SZ, data=self.position),
        )

    @classmethod
    def from_tree(cls, tree: RegistryKey) -> "Position | None":
        value = tree.get_value(ATTRIBUTE_NAME)
        if value is not None and isinstance(value.data, str):
            assert value.data.lower() in ("top", "bottom"), f"Bad position value: {value.data}"

            return Position(
                "Top" if value.data.lower() == "top" else "Bottom",
            )
        return None
