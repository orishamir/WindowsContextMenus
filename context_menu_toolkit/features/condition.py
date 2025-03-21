from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from context_menu_toolkit.conditions import ICondition
from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import DataType, RegistryKey, RegistryValue


@dataclass
class Condition(IFeature):
    """Add a condition for the context menu to display.

    See context_menu_toolkit.conditions for available conditions.

    Attributes:
        selection_model: Specifies the amount of simultaneously selected items the context menu supports.
            For example, when selecting SelectionModelAmount.SINGLE, if more than 1 item (file/folder/etc.)
            is selected, right-clicking would not display the menu.[^1]

    References:
        [^1]: <https://learn.microsoft.com/en-us/windows/win32/shell/how-to-employ-the-verb-selection-model>
        [^2] [MSDN - Getting Dynamic Behavior for Static Verbs by Using Advanced Query Syntax](https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax)

    Example:
        ```python
        from context_menu_toolkit.comparers import GreaterThan
        from context_menu_toolkit.conditions import FileSize

        ConditionFeature(
            condition=FileSize(
                comparer=GreaterThan("20MB"),
            ),
        )
        ```
    """
    selection_model: Literal["single", "fifteen_items_max", "hundred_items_max"]
    condition: ICondition

    def apply_registry(self, tree: RegistryKey) -> None:
        self._apply_selection_model(tree)
        self._apply_aqs_condition(tree)

    def _apply_selection_model(self, tree: RegistryKey) -> None:
        if self.selection_model == "single":
            amount = "Single"
        elif self.selection_model == "fifteen_items_max":
            amount = "Document"
        else:
            amount = "Player"

        tree.values.append(
            RegistryValue(name="MultiSelectModel", type=DataType.REG_SZ, data=amount),
        )

    def _apply_aqs_condition(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="AppliesTo", type=DataType.REG_SZ, data=self.condition.to_aqs_string()),
        )
