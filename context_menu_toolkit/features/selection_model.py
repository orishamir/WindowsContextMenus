from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class SelectionModel(IFeature):
    r"""Specifies the amount of simultaneously selected items the context menu supports.

    For example, when selecting SelectionModelAmount.SINGLE, if more than 1 item (file/folder/etc.)
    is selected, right-clicking would not display the menu.

    Attributes:
        amount: The amount from the SelectionModelAmount enum.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/how-to-employ-the-verb-selection-model>
    """
    amount: SelectionModelAmount

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data=self.amount),
        )


class SelectionModelAmount(StrEnum):
    """Possible values for selection model.

    For example, when selecting SelectionModelAmount.SINGLE, if more than 1 item (file/folder/etc.)
    is selected, right-clicking would not display the menu.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/how-to-employ-the-verb-selection-model>
    """
    SINGLE = "Single"
    FIFTEEN_ITEMS_MAX = "Document"
    HUNDRED_ITEMS_MAX = "Player"
