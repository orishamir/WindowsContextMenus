from dataclasses import dataclass
from typing import Literal

from context_menu_toolkit.registry.registry_structs import DataType, RegistryKey, RegistryValue
from context_menu_toolkit.registry.shell_attributes.ishellattribute import IShellAttribute


@dataclass
class SelectionModel(IShellAttribute):
    r"""Specifies the amount of simultaneously selected items the context menu supports.

    For example, when selecting SelectionModelAmount.SINGLE, if more than 1 item (file/folder/etc.)
    is selected, right-clicking would not display the menu.

    Attributes:
        Model: Single - One item.
                Document - Maximum of 15 items.
                Player - Maximum of 100 items.

    References:
        [^1]: <https://learn.microsoft.com/en-us/windows/win32/shell/how-to-employ-the-verb-selection-model>
    """
    model: Literal["Single", "Document", "Player"]

    def apply_to_tree(self, tree: RegistryKey) -> None:
        tree.add_value(
            RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data=self.model),
        )
