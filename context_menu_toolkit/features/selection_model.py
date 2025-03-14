from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class SelectionModel(IFeature):
    r"""Specifies the amount of selected items the context menu supports.

    Attributes:
        amount: The amount from the SelectionModelAmount enum.
    """
    amount: SelectionModelAmount

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data=self.amount),
        )


class SelectionModelAmount(StrEnum):
    """Possible values for selection model.

    References:
        <https://learn.microsoft.com/en-us/windows/win32/shell/how-to-employ-the-verb-selection-model>
    """
    SINGLE = "Single"
    MULTIPLE = "Player"
    FIFTEEN_ITEMS = "Document"
